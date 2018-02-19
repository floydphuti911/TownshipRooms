from django.contrib import admin
from core_platform.models import *

admin.site.register(RoomManager)
admin.site.register(Room)
admin.site.register(Tenant)
admin.site.register(RoomLease)