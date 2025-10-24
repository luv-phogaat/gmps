from django.contrib import admin
from django.utils.html import format_html
from .models import Image
# from django.contrib.auth.models import Group

# Declaring models import
from .models import Contact, ResultPdf

class ContactAdmin(admin.ModelAdmin):
    # ...
    list_display = ('name', 'email', 'mob', 'message', 'date')
    list_filter = ('date',)

class ResultPdfAdmin(admin.ModelAdmin):
    list_display = ( 'linkname', 'link', 'date')


class ImageAdmin(admin.ModelAdmin):

    # def image_tag(self, obj):
    #     return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))

    list_display = ['name','image']


# Register your models here.

admin.site.register(Contact, ContactAdmin)
admin.site.register(ResultPdf, ResultPdfAdmin)
admin.site.register(Image, ImageAdmin)


# admin.site.unregister(Group)