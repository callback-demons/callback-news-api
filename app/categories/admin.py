from django.contrib import admin
from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'color', 
        'picture',   
        'created', 
        'deleted'
    )

    ordering = ('name',)
    readonly_fields = ('created', 'deleted')
    search_fields = ('name',)

