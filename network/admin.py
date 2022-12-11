from django.forms.models import modelform_factory
from django.contrib import admin
from .models import *

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    filter_horizontal = ("follow",)


admin.site.register(Posts)
admin.site.register(Profile, ProfileAdmin)
