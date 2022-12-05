from django.contrib import admin
from .models import *
from nested_admin import NestedStackedInline, NestedModelAdmin

# Register your models here.
class subFeatureInline(NestedStackedInline):
    model = SubFeatures
    extra = 1
    
class FeatureInline(NestedStackedInline):
    model = Features
    extra = 3
    inlines = [subFeatureInline]

class HeadingsAdmin(NestedModelAdmin):
    fields = ['heading', 'subHeading', 'icon', 'btnApp', 'btnCode', 'videoLink']
    inlines = [FeatureInline]

admin.site.register(Headings, HeadingsAdmin)