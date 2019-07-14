from django.contrib import admin
from booktest.models import *


# Register your models here.
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'pub_date', 'read', 'comment', 'isDelete']


admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo)