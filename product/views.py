# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext
from product.models import SubCategory, MainCategory, Category, Product

def product_info(request):
    print "Product information"
    return render_to_response("home/products.html", context_instance=RequestContext(request))

def showCategory(request, mainCategory="", category=None, subCategory=None):
    #print category
    sclists = []
    sclist = {}
    product_list = {}
    if len(mainCategory) > 0:
        mc = MainCategory.objects.get(CategoryName=mainCategory)
        sc = SubCategory.objects.filter(MainCatID = mc.MainCatID)
        for subCat in sc:
            sclist[subCat.CategoryName.replace("men ", "")+"/"] = subCat.CategoryName.replace("men ", "")
    
        sclists.append(sclist)
    
    if category is not None:
        if subCategory is not None:
            sc = SubCategory.objects.filter(CategoryName=category, MainCatID=mc.pk)
            cat = Category.objects.get(MainCatID=mc.pk, SubCatID=sc.values()[0]['SubCatID'], CategoryName=subCategory)
            product_list = Product.objects.filter(CategoryID = cat.pk)
            
            # return list of products to Display
            return render_to_response("home/products.html", 
                                  {
                                    'product_list' : product_list,
                                   }, 
                                  context_instance=RequestContext(request))
        
        sc = SubCategory.objects.filter(CategoryName=category, MainCatID=mc.pk)
        cat = Category.objects.filter(MainCatID=mc.pk, SubCatID=sc.values()[0]['SubCatID'])
        #print cat.values()
        return render_to_response("home/category.html", 
                                  {
                                    'Categories' : cat,
                                    'MainCat': mainCategory,
                                    'SubCat' : category,
                                   }, 
                                  context_instance=RequestContext(request))
    
    return render_to_response("home/category.html", 
                              {
                                'subCategories' : sclists, 
                                'MainCat': mainCategory,
                                'SubCat' : category,
                              }, 
                              context_instance=RequestContext(request)
                             )

def view_products(request, mainCategory="", category=None, subCategory=None, productID=None):
    
    product_info = Product.objects.filter(ProductID = productID)
    print product_info.values()
    return render_to_response("home/products.html", { "product_info" : product_info[0] }, context_instance=RequestContext(request))


