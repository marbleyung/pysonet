from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'created_at', 'id', 'times_viewed')


class CommentAdmin(MPTTModelAdmin, admin.ModelAdmin):
    list_display = ('author', 'post', 'created_at', 'edited_at', 'is_edited', 'id')
    mptt_level_indent = 15


admin.site.register(Post)
admin.site.register(Comment, CommentAdmin)
