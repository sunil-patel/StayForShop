# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

def cart_details(request):
    return render_to_response("home/cart.html", context_instance=RequestContext(request))
    