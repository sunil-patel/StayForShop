from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
    return render_to_response("home/home.html", context_instance=RequestContext(request))

def paypal(request):
    return render_to_response("paypal/setcheckout.html", context_instance=RequestContext(request))

def showMenCategory(request):
    return render_to_response("home/category.html", context_instance=RequestContext(request))