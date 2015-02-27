from django.contrib import admin

from cdr_tables.models import Cdr
from cdr_tables.models import Musiconhold
from cdr_tables.models import QueueLog
from cdr_tables.models import QueueMemberTable
from cdr_tables.models import QueueTable
from cdr_tables.models import SipDevices
from cdr_tables.models import Voicemail

admin.site.register(Cdr)
admin.site.register(Musiconhold)
admin.site.register(QueueTable)
admin.site.register(QueueLog)
admin.site.register(QueueMemberTable)
admin.site.register(Voicemail)
admin.site.register(SipDevices)

