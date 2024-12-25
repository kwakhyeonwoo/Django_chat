from django.contrib import admin
from .models import *

from a_rtchat.models import ChatGroup

admin.site.register(ChatGroup)
admin.site.register(GroupMessage)
