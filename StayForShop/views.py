from django.shortcuts import render_to_response
from django.template import RequestContext
from product.models import SubCategory, MainCategory

def home(request):
    return render_to_response("home/home.html", context_instance=RequestContext(request))

def paypal(request):
    return render_to_response("paypal/setcheckout.html", context_instance=RequestContext(request))

def showMenCategory(request):
    mc = MainCategory.objects.get(CategoryName="Men")
    sc = SubCategory.objects.filter(MainCatID = mc.MainCatID)
    sclists = []
    sclist = {}
    for subCat in sc:
        sclist[subCat.CategoryName.replace("men ", "")+"/"] = subCat.CategoryName.replace("men ", "")
    
    sclists.append(sclist)
    return render_to_response("home/category.html", {'subCategories' : sclists,}, context_instance=RequestContext(request))

def showMenShoes(request):
    return render_to_response("home/category.html", context_instance=RequestContext(request))