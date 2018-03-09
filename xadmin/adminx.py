from __future__ import absolute_import
import xadmin
from .models import UserSettings, Log
from xadmin.layout import *

from django.utils.translation import ugettext_lazy as _, ugettext

class UserSettingsAdmin(object):
    model_icon = 'fa fa-cog'
    hidden_menu = True

xadmin.site.register(UserSettings, UserSettingsAdmin)

class LogAdmin(object):

    def link(self, instance):
        if instance.content_type and instance.object_id and instance.action_flag != 'delete':
            admin_url = self.get_admin_url('%s_%s_change' % (instance.content_type.app_label, instance.content_type.model), 
                instance.object_id)
            return "<a href='%s'>%s</a>" % (admin_url, _('Admin Object'))
        else:
            return ''
    link.short_description = ""
    link.allow_tags = True
    link.is_column = False

    list_display = ('action_time', 'user', 'ip_addr', '__str__', 'link')
    list_display = ('action_time', 'user', 'ip_addr', 'link')
    list_filter = ['user', 'action_time']
    search_fields = ['ip_addr', 'message']
    model_icon = 'fa fa-cog'

    readonly_fields = ('action_time','user','ip_addr','content_type','object_id','message','action_flag','object_repr')

    # action_time = models.DateTimeField(
    #     _('action time'),
    #     default=timezone.now,
    #     editable=False,
    # )
    # user = models.ForeignKey(
    #     AUTH_USER_MODEL,
    #     models.CASCADE,
    #     verbose_name=_('user'),
    # )
    # ip_addr = models.GenericIPAddressField(_('action ip'), blank=True, null=True)
    # content_type = models.ForeignKey(
    #     ContentType,
    #     models.SET_NULL,
    #     verbose_name=_('content type'),
    #     blank=True, null=True,
    # )
    # object_id = models.TextField(_('object id'), blank=True, null=True)
    # object_repr = models.CharField(_('object repr'), max_length=200)
    # action_flag = models.CharField(_('action flag'), max_length=32)
    # message = models.TextField(_('change message'), blank=True)

xadmin.site.register(Log, LogAdmin)
