from django.conf.urls.defaults import *
 
urlpatterns = patterns('calendars.views',
    url(r'^$', 'month', name='calendars_current_month'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{2})/$', 'month', name='calendars_single_month'),
)
