from django.contrib import admin

from .models import ResultImage

class ResultImageAdmin(admin.ModelAdmin):

    list_display = ['id', 'image', 'entry_image', 'added_at', 'modified',]
    search_fields = ['image', 'entry_image', 'added_at', 'modified']
    list_filter = ['added_at', 'modified']
    list_display_links = ('id', 'image', 'entry_image')
 
admin.site.register(ResultImage, ResultImageAdmin)