from django.contrib import admin
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'title', 
        'author', 
        'source', 
        'category', 
        'created',
        'published',
        'deleted',
        'user'
    )

    ordering = ('created', 'source')
    readonly_fields = ('created', 'deleted', 'updated')
    search_fields = ('title', 'source', 'category', 'author')

