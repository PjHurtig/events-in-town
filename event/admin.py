from django.contrib import admin
from .models import Post


# post admin class to generate slug with prepopulated fields, display important
# statuses in the admin panel, filter and search the posts
# initial code based on the django blog walkthrough project and adapted to
# fit this sites functions
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('event_date', 'event_time', 'artist',)
    }
    list_filter = ('status', 'created_on', 'updated_on', 'event_date', 'area')
    list_display = ('status', 'created_on', 'updated_on', 'event_date', 'area')
    search_fields = ['about', 'title', 'artist']
