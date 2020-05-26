from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'user', 'news', 'created', 'deleted')
    ordering = ('created',)
    readonly_fields = ('created', 'deleted')
    search_fields = ('user',)

