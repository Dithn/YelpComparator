from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'yelphelp.comparison.views.home', name='home'),
    url(r'^search/$', 'yelphelp.comparison.views.search', name='search'),
    url(r'^compare/$', 'yelphelp.comparison.views.compare', name='compare'),
# /blahblah
    #url(r'^blahblah$', 'yelphelp.views.home'),

    # url(r'^yelphelp/', include('yelphelp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
