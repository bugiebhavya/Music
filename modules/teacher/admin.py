from django.contrib import admin
from .models import Teacher
# Register your models here.

class TeacherAdmin(admin.ModelAdmin):
	fields = ('username', 'email', 'dob', 'password', 'phone_number','profile_image', 'gender', 'level', 'city', 'experience', 'country', 'time_zone', 'language', 'video_file', 'short_introduction', 'about')
	def get_queryset(self, request):
		qs = super(TeacherAdmin, self).get_queryset(request)
		return qs.filter(is_superuser=False)


admin.site.register(Teacher,TeacherAdmin)

