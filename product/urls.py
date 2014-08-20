from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^(men)/$', 'product.views.showCategory', name="men"),
    url(r'^(men)/(shoes)/$', 'product.views.showCategory', name="mshoes"),
    url(r'^(men)/(bags)/$', 'product.views.showCategory', name="mbags"),
    url(r'^(men)/(jewellery)/$', 'product.views.showCategory', name="mjewell"),
    url(r'^(men)/(sunglasses)/$', 'product.views.showCategory', name="msun"),
    url(r'^(men)/(clothes)/$', 'product.views.showCategory', name="mclothes"),
    url(r'^(men)/(accessories)/$', 'product.views.showCategory', name="maccess"),
    url(r'^(men)/(fragrances)/$', 'product.views.showCategory', name="mfrag"),
    url(r'^(men)/(watches)/$', 'product.views.showCategory', name="mwatch"),
    url(r'^(?P<mainCategory>\w+)/(?P<category>\w+)/(?P<subCategory>\w+\s?\w+)/$', 'product.views.showCategory'),
    url(r'^(?P<mainCategory>\w+)/(?P<category>\w+)/(?P<subCategory>\w+\s?\w+)/(?P<productID>\d+)$', 'product.views.view_products'),
    
    # url(r'^StayForShop/', include('StayForShop.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)