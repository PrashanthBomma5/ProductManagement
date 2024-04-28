from django.contrib import admin

# Register your models here.
from .models import *
class productadmin(admin.ModelAdmin):
    list_display=('id','name','price','is_published','created_at')
    list_display_links=('id','name',)
    list_filter=('price','created_at',)
    list_editable=('is_published',)
    search_fields=('name',)
    ordering=('price',)
admin.site.register(Product,productadmin)
admin.site.register(Category)


