
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import AuthorForm, Author, Book, CustomerForm
from django.forms.models import modelform_factory
from django.forms.formsets import formset_factory


# list of mobile User Agents
mobile_uas = [
    'w3c ','acs-','alav','alca','amoi','audi','avan','benq','bird','blac',
    'blaz','brew','cell','cldc','cmd-','dang','doco','eric','hipt','inno',
    'ipaq','java','jigs','kddi','keji','leno','lg-c','lg-d','lg-g','lge-',
    'maui','maxo','midp','mits','mmef','mobi','mot-','moto','mwbp','nec-',
    'newt','noki','oper','palm','pana','pant','phil','play','port','prox',
    'qwap','sage','sams','sany','sch-','sec-','send','seri','sgh-','shar',
    'sie-','siem','smal','smar','sony','sph-','symb','t-mo','teli','tim-',
    'tosh','tsm-','upg1','upsi','vk-v','voda','wap-','wapa','wapi','wapp',
    'wapr','webc','winw','winw','xda','xda-'
    ]
 
mobile_ua_hints = [ 'SymbianOS', 'Opera Mini', 'iPhone' ]

def mobileBrowser(request):
    ''' Super simple device detection, returns True for mobile devices '''
 
    mobile_browser = False
    print request.META['HTTP_USER_AGENT'].lower()[0:4]
    ua = request.META['HTTP_USER_AGENT'].lower()[0:4]
 
    if (ua in mobile_uas):
        mobile_browser = True
    else:
        for hint in mobile_ua_hints:
            if request.META['HTTP_USER_AGENT'].find(hint) > 0:
                mobile_browser = True
 
    return mobile_browser
 

def home(request):
    if mobileBrowser(request):
        print "Mobile Browser"
    
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