from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group
# Register your models here.

class UserAdmin(admin.ModelAdmin):
	list_display = ('username', 'email', 'dob', 'is_active')
	fields = ('username', 'email', 'dob', 'password', 'phone_number', 'is_active')
	def get_queryset(self, request):
		qs = super(UserAdmin, self).get_queryset(request)
		return qs.filter(is_superuser=False)

admin.site.unregister(Group)
admin.site.register(User,UserAdmin)
