# -*- coding:utf-8 -*-
from django.forms import ModelForm
from spw_extension.models import *


class ExtensionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ExtensionForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'input-sm form-control'

    class Meta:
        model = Extension
        fields = (
            'spw_display_name',
            'spw_username',
            'spw_passwd',
            'spw_email',
            'spw_call_group',
            'spw_pickup_group',
            'spw_active',
        )

        # widgets = {
        #     'spw_display_name': 'form-controls',
        # }

# class UsuarioForm(ModelForm):
#     class Meta:
#         model = Usuario
#         fields = ('nome', 'nomeguerra', 'ramal')
#         labels = {
#             'name': ('Número do ramal'),
#             'nomeguerra': (u'Nome de guerra'),
#         }
#         # help_texts = {
#         #     'name': _('Some useful help text.'),
#         # }
#         # error_messages = {
#         #     'name': {
#         #         'max_length': _("This writer's name is too long."),
#         #     },
#         # }
