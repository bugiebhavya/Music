from django.contrib import admin
from .models import Booking, Media
# Register your models here.

class BookingAdmin(admin.ModelAdmin):
	list_display=['user', 'teacher', 'booking_status']

	# def has_add_permission(self, obj):
	# 	return False

admin.site.register(Booking, BookingAdmin)


# class MusicGenreAdmin(admin.ModelAdmin):
# 	list_display=['name', 'created_at']

# admin.site.register(MusicGenre, MusicGenreAdmin)

# class InstrumentAdmin(admin.ModelAdmin):
# 	list_display=['name', 'created_at']

# admin.site.register(Instrument, InstrumentAdmin)


class MediaAdmin(admin.ModelAdmin):
	list_display=['booking', 'video_file']

	# def has_add_permission(self, obj):
	# 	return False

admin.site.register(Media, MediaAdmin)