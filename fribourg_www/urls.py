from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^$', 'coffin.views.generic.simple.direct_to_template', {'template': 'index.html'}, name='index'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^%s(?P<path>.*)$' % (settings.MEDIA_URL[1:]), 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
