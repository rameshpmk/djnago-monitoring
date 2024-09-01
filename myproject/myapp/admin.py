from django.contrib import admin
from .models import IPAddress, PingResult
# Register your models here.

admin.site.register(IPAddress)
admin.site.register(PingResult)
