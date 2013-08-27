from django.conf.urls import patterns, include, url
from mapvis.views import hello, mapapp
from bobbin_lace_association.views import memb_reg
 
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
 
 
urlpatterns = patterns('',
                        url('^hello/$', hello),
                        url('^mapapp/$', mapapp),
                        url('^$', mapapp),
                        url('^bobbin_lace/memb_reg/$', memb_reg),
)