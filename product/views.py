# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext

def product_info(request):
    print "Product information"
    return render_to_response("home/products.html", context_instance=RequestContext(request))