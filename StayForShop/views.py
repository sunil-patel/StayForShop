from django.shortcuts import render_to_response
from django.template import RequestContext
from product.models import SubCategory, MainCategory, Category

def home(request):
    return render_to_response("home/home.html", context_instance=RequestContext(request))

def paypal(request):
    return render_to_response("paypal/setcheckout.html", context_instance=RequestContext(request))

def showCategory(request, mainCategory="men", category="shoes"):
    print category
    if len(mainCategory) > 0:
        mc = MainCategory.objects.get(CategoryName=mainCategory)
        sc = SubCategory.objects.filter(MainCatID = mc.MainCatID)
        sclists = []
        sclist = {}
        for subCat in sc:
            sclist[subCat.CategoryName.replace("men ", "")+"/"] = subCat.CategoryName.replace("men ", "")
    
        sclists.append(sclist)
        
    
    if category is not None:
        sc = SubCategory.objects.filter(CategoryName=category, MainCatID=mc.pk)
        cat = Category.objects.filter(MainCatID=mc.pk, SubCatID=sc.values()[0]['SubCatID'])
        print cat.values()
        return render_to_response("home/category.html", {'Categories' : cat,}, context_instance=RequestContext(request))
    return render_to_response("home/category.html", {'subCategories' : sclists,}, context_instance=RequestContext(request))

#def showMenShoes(request):
#    return render_to_response("home/category.html", context_instance=RequestContext(request))