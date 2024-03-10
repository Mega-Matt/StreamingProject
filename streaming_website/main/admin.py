from django.contrib import admin

# Register your models here.
from .models import Channel, Tag

admin.site.register(Channel)
admin.site.register(Tag)
