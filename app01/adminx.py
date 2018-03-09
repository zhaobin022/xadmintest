import xadmin
from xadmin import views
from django import forms
from django.contrib.auth.models import Group
from .models import UserProfile
from xadmin.plugins.auth import GroupAdmin


class BaseSetting(object):
    enable_themes  = True
    use_bootswatch = True

class GlobalSettings(object):
    site_title = 'my background'
    site_footer = 'my site'
    menu_style = "accordion"


class GroupAdminForm(forms.ModelForm):
    user_set = forms.ModelMultipleChoiceField(queryset=UserProfile.objects.all(),
                                           # widget=FilteredSelectMultiple('Users11', False),
                                           # attrs={
                                           #     'placeholder': "请在表名前加上schema，如hospital要写成p95169.hospital",
                                           #     'rows': 5,
                                           #     'style': "width:100%",
                                           # },
                                           required=False)
    class Meta:
        model = Group
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance', None)
        if instance is not None:
            initial = kwargs.get('initial', {})
            initial['user_set'] = instance.user_set.all()
            kwargs['initial'] = initial
        super(GroupAdminForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        group = super(GroupAdminForm, self).save(commit=commit)

        if commit:
            group.user_set = self.cleaned_data['user_set']
        else:
            old_save_m2m = self.save_m2m
            def new_save_m2m():
                old_save_m2m()
                group.user_set = self.cleaned_data['user_set']
            self.save_m2m = new_save_m2m
        return group


class MyGroupAdmin(GroupAdmin):
    form = GroupAdminForm
    # filter_horizontal = ('user_set','permissions')
    style_fields = {
        'permissions': 'm2m_transfer',
        'user_set': 'm2m_transfer',
    }

    #
    # fieldsets = (
    #     (None, {'fields': ('name','alias',)}),
    #     (None, {'fields': ('permissions','users','jenkins_job')}),
    # )
    # def get_field_attrs(self, db_field, **kwargs):
    #     attrs = super(GroupAdmin, self).get_field_attrs(db_field, **kwargs)
    #     if db_field.name == 'permissions':
    #         attrs['form_class'] = PermissionModelMultipleChoiceField
    #     elif db_field.name == 'users':
    #         attrs['form_class'] = ModelMultipleChoiceField
    # #
    #     return attrs

# class UserProfileAdmin(object):
#     # filter_horizontal = ('user_set','permissions')
#     style_fields = {
#         'user_permissions': 'm2m_transfer',
#         'groups': 'm2m_transfer',
#     }

xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)
xadmin.site.unregister(Group)
xadmin.site.register(Group,MyGroupAdmin)
# xadmin.site.unregister(UserProfile)
# xadmin.site.register(UserProfile,UserProfileAdmin)
