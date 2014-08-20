
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import AuthorForm, Author, Book, CustomerForm
from django.forms.models import modelform_factory
from django.forms.formsets import formset_factory

def home(request):
    return render_to_response("home/home.html", context_instance=RequestContext(request))

def paypal(request):
    return render_to_response("paypal/setcheckout.html", context_instance=RequestContext(request))


def test_form(request):
    
    #form = formset_factory(AuthorForm);
    form = formset_factory(CustomerForm)
    #name = form.cleaned_data['name']
    #title = form.cleaned_data['title']
    #print form.as_p()
    return render_to_response("home/temp.html", {'form': form}, context_instance=RequestContext(request))

def test_form_save(request):
    if request.method == "GET":
        #form = AuthorForm()
        form = formset_factory(CustomerForm)
    else:
        #form = AuthorForm(request.POST)
        form = CustomerForm(request.POST)
        print form.as_p()
        if form.is_valid():
            print "Validated"
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            email = form.cleaned_data['email']
            phone= form.cleaned_data['phone']
            #title = form.cleaned_data['title']
            #birth_date = form.cleaned_data['birth_date']
            #author = Author.objects.create(name=name, title=title, birth_date=birth_date)
            #author.save()
            
            #form = modelform_factory(Book, from=BookForm, fields=('name'))
            
    return render_to_response("home/temp.html", {'form': form}, context_instance=RequestContext(request))