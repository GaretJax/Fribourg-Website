from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import MonthCalendarPlugin
from django.utils.translation import ugettext_lazy as _

import datetime
from schedule.conf.settings import GET_EVENTS_FUNC
from schedule.periods import Month, weekday_names

class CMSMonthCalendarPlugin(CMSPluginBase):
        model = MonthCalendarPlugin
        name = _("Monthly calendar")
        render_template = "calendars/month.html"
        
        def render(self, context, instance, placeholder):
            date = context.get('date', datetime.datetime.now())
            
            event_list = []
            for calendar in instance.calendars_to_display.all():
                event_list += GET_EVENTS_FUNC(context['request'], calendar)
            
            period = Month(event_list, date)
            
            context.update({
                'date': date,
                'events': event_list,
                'period': period,
                'calendar': instance.calendars_to_display.all(),
                'weekday_names': weekday_names,
                'display_details': instance.display_details,
            })
            
            return context

plugin_pool.register_plugin(CMSMonthCalendarPlugin)