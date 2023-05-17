from django.contrib import admin
from .models import News,Category

# Register your models here.

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title','slug','publish_time','status']
    list_filter = ['status','publish_time','created_time']
    prepopulated_fields = {'slug':('title',)}
    date_hierarchy = 'publish_time'
    search_fields = ['title','body']
    ordering = ['status','publish_time']



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']