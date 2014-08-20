# Create your views here.

from django.shortcuts import render_to_response, resolve_url
from django.contrib import auth
from django.shortcuts import  HttpResponseRedirect, HttpResponse, redirect
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
import datetime
from django.contrib.auth import logout
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from Users.models import Customer
from product.models import SubCategory, MainCategory, Category

def set_cookie(response, key, value, days_expire = 7):
    if days_expire is None:
        max_age = 365 * 24 * 60 * 60  #one year
    else:
        max_age = days_expire * 24 * 60 * 60 
        expires = datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age), "%a, %d-%b-%Y %H:%M:%S GMT")
        response.set_cookie(key, value, max_age=max_age, expires=expires)
    
def authentication(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
   
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        request.session["username"] = username
        request.session["firstname"] = user.first_name
        
        # Redirect to a success page.
        #return HttpResponseRedirect("/", request)
        return redirect("/", context_instance=RequestContext(request))
    else:
        # Show an error page
        return render_to_response("home/login.html", 
                                  {'error' : 'Login Failed', 'Reason' : 'Username or Password is incorrect, please try again'}, 
                                  context_instance=RequestContext(request))
        
@login_required(login_url='/user/login/')
def logout(request):
    try:
        request.session['username']=""
        auth.logout(request)
        return HttpResponseRedirect("/")
    except KeyError, e:
        print dir(e)
        print "Logout error", e
        HttpResponseRedirect("/")
    
def login_page(request):
    return render_to_response("home/login.html", context_instance=RequestContext(request))


def signup_page(request):
    return render_to_response("home/signup.html", context_instance=RequestContext(request))

def register(request):
    user = {}
    try :
        new_user = User.objects.get(username=request.POST['email'])
        user = {
                'first_name': request.POST['first_name'],
                'last_name': request.POST["last_name"],
                'email': request.POST['email'],
                'mobile':request.POST['mobile'],
                'message' : 'You are already registered with us. Try logging in'
                }
        return render_to_response("home/signup.html", 
                                  user,
                                  context_instance=RequestContext(request))
    except Exception:
        pass
    if request.POST['password'] != request.POST['conf_pass']:
        return render_to_response("home/signup.html", {"pass_error": "Password did not Match"}, context_instance=RequestContext(request))
    
    new_user = User(username=request.POST["email"])
    new_user.first_name = request.POST["first_name"]
    new_user.last_name = request.POST["last_name"]
    new_user.email = request.POST["email"]
    new_user.is_active = True
    from datetime import date
    new_user.date_joined = date.today()
    new_user.is_superuser = False
    new_user.is_staff = False
    new_user.set_password(request.POST['password'])
    new_user.save()
    
    group = Group.objects.get(name='Customer') 
    group.user_set.add(new_user)                  # assign user as Customer.
    group.save()
    
    id = User.objects.get(username=request.POST["email"])    #Add into Customer Schema
    new_cust = Customer(ID_id=id.pk)
    new_cust.Phone = request.POST['mobile']
    new_cust.DateEntered = date.today()
    new_cust.save()
    
    '''
        After successfully new user validation, below is allow the authentication through out the application.
        And store the user to session.
    '''
    user = auth.authenticate(username=request.POST["email"], password=request.POST['password'])
    auth.login(request, user)
    request.session["username"] = request.POST["email"]
    request.session["firstname"] = request.POST["first_name"]

  