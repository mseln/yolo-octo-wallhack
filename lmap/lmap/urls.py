from django.conf.urls import patterns, include, url
from mapvis import views
from debugging import debug_server

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
		(r'^$', views.mapapp),
		(r'^hello/$', views.hello),
		(r'^mapapp/$', views.mapapp),
		(r'^debug/$', debug_server.debug),
    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)
