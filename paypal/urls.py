from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^setcheckout/$', 'paypal.views.setcheckout', 
         name = "paypal_setcheckout"),
    url(r'^docheckout/$', 'paypal.views.docheckout', 
        name = "paypal_docheckout"),                       
    url(r'^dorefund/$', 'paypal.views.dorefund', 
        {'success_url': 'http:/127.0.0.1:8000/payment/success/',
         'error_url': 'http:/127.0.0.1:8000/payment/error/',
         },name = "paypal_dorefund"),
    
    url(r'^cancel/$', 'paypal.views.cancel_page', name = "base_cancel"),
    url(r'^success/$', 'paypal.views.success_page', name = "base_success"),                       
    url(r'^error/$', 'paypal.views.error_page', name = "base_error"),
    
)