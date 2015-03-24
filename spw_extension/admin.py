from django.contrib import admin
from spw_extension.models import *


# class Admin(admin.ModelAdmin):
#     '''
#         Admin View for 
#     '''
#     list_display = ('',)
#     list_filter = ('',)
#     inlines = [
#         Inline,
#     ]
#     raw_id_fields = ('',)
#     readonly_fields = ('',)
#     search_fields = ['']

# admin.site.register(, Admin)

admin.site.register(Extension)
admin.site.register(GroupExtension)