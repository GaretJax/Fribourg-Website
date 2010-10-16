from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class CalendarHook(CMSApp):
    name = _("Calendar")
    urls = ["calendars.urls"]

apphook_pool.register(CalendarHook)
