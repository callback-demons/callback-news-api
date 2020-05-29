from django.contrib import admin
from .models import Media

@admin.register(Media)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'url', 'created', 'deleted')
    #ordering = ('created',)
    readonly_fields = ('created', 'deleted')
    search_fields = ('user',)

