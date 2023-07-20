from django.contrib import admin
from .models import Post
from django.utils.text import slugify


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('event_date', 'event_time', 'artist',)
    }
    list_filter = ('status', 'created_on', 'updated_on', 'event_date', 'area')
    list_display = ('status', 'created_on', 'updated_on', 'event_date', 'area')
    search_fields = ['about', 'title', 'artist']
