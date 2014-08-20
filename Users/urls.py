from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    
    url(r'login/$', 'Users.views.login_page', name="login"),
    url(r'authentication/$', 'Users.views.authentication', name='authentication'),
    url(r'logout/$', 'Users.views.logout', name="logout"),
    url(r'signup/$', 'Users.views.signup_page', name="signup"),
    url(r'register/$', 'Users.views.register', name="register"),
    
   
    # url(r'^StayForShop/', include('StayForShop.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)