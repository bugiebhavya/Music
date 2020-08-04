from django.contrib import admin
from .models import Ratings, StaticPages, MusicGenre, Instrument, EmailTemplate
# Register your models here.



class EmailTemplateAdmin(admin.ModelAdmin):
	list_display=['template_name', 'email_subject', 'created_at']

admin.site.register(EmailTemplate, EmailTemplateAdmin)


class StaticPagesAdmin(admin.ModelAdmin):

	list_display=['template_name', 'created_at']

admin.site.register(StaticPages, StaticPagesAdmin)


class RatingAdmin(admin.ModelAdmin):
	list_display=['teacher', 'user', 'rating', 'comment', 'is_verified']

	def has_add_permission(self, obj):
		return False

admin.site.register(Ratings, RatingAdmin)


class MusicGenreAdmin(admin.ModelAdmin):
	list_display=['name', 'created_at']

admin.site.register(MusicGenre, MusicGenreAdmin)

class InstrumentAdmin(admin.ModelAdmin):
	list_display=['name', 'created_at']

admin.site.register(Instrument, InstrumentAdmin)