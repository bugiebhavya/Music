from django.contrib import admin
from .models import Teacher, TeacherDocument
# Register your models here.

class CertificateInline(admin.StackedInline):
    model = TeacherDocument
    extra = 1
    max_num = 5


class TeacherAdmin(admin.ModelAdmin):
	list_display=('username', 'email', 'dob', 'phone_number', 'experience', 'level', 'is_active', 'is_verified')
	inlines = [CertificateInline,]
	fields = ('username', 'email', 'dob', 'password', 'phone_number','profile_image', 'gender', 'level', 'city', 'experience', 'country', 'time_zone', 'language', 'video_file', 'music_genre', 'short_introduction', 'about', 'is_active', 'is_verified')
	search_fields = ('username', 'email', 'dob', )
	def get_queryset(self, request):
		qs = super(TeacherAdmin, self).get_queryset(request)
		return qs.filter(is_superuser=False)


admin.site.register(Teacher,TeacherAdmin)

