from django.contrib import admin
from .models import poll, Option
# Register your models here.
admin.site.register(poll)
admin.site.register(Option)