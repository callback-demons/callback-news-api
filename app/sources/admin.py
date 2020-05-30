from django.contrib import admin
from .models import Source

@admin.register(Source)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'feed_type', 'feed_url')

    ordering = ('name', 'created')
    readonly_fields = ('created', 'deleted')
    search_fields = ('name', 'deleted')

