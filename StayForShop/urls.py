from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns ('',
    # Examples:
    url(r'^$', 'StayForShop.views.home', name='home'),
    url(r'^user/', include('Users.urls')),
    url(r'^products/t-shirt/$', 'product.views.product_info', name='products'),
    url(r'^cart/$', 'cart.views.cart_details', name="cart"),
    url(r'^payment/', include('paypal.urls')),
    url(r'^checkout/$', 'StayForShop.views.paypal', name='checkout'),
    url(r'^(?P<mainCategory>\w*?)/((?P<category>\w*?)/)?$', 'StayForShop.views.showCategory'),
    #url(r'^men/shoes/$', 'StayForShop.views.showMenShoes', name="shoes"),
    #url(r'^men/bags/$', 'StayForShop.views.showMenShoes', name="bags"),
    
    #url(r'^checkout/', include('paypal_express_checkout.urls')),
    
    # url(r'^StayForShop/', include('StayForShop.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
