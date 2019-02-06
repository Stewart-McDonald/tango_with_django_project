
from django.contrib import admin
from rango.models import Category, Page
# Register your models here.


class PageAdmin():
    list_display = ('title', 'category', 'url')

admin.site.register(Page)

admin.site.register(Page, PageAdmin)
admin.site.register(Category)

