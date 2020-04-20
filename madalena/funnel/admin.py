from django.contrib import admin

from .models import EntryImages

class EntryImagesAdmin(admin.ModelAdmin):

    list_display = ['id', 'image', 'resized', 'added_at', 'modified',]
    exclude = ('resized', 'height', 'width',)
    search_fields = ['image', 'added_at', 'modified']
    list_filter = ['added_at', 'modified']
    list_display_links = ('id', 'image')
 
admin.site.register(EntryImages, EntryImagesAdmin)