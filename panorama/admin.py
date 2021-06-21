from django.contrib import admin
from .models import Room, ComponentImage

class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image')
    list_filter = ('title',)
    list_display_links = ('id', 'title')
    list_per_page = 10

admin.site.register(Room, RoomAdmin)


class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'room', 'image')
    list_filter = ('title', 'room')
    list_display_links = ('id', 'title', 'room')
    list_per_page = 10
admin.site.register(ComponentImage, ImageAdmin)