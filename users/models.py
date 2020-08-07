from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
import pdb


class User(AbstractUser):
	ROLE = (
		("STUDENT", 'Student'),
		("TEACHER", 'Teacher')
	)
	class Meta:
		verbose_name =_("Student")
		verbose_name_plural = _("Students")

	username = models.CharField(verbose_name=_('Username'), max_length=100, unique=True)
	email = models.EmailField(verbose_name=_('Email'),max_length=200,blank=False,null=False)
	dob = models.DateField(verbose_name=_("Date of Birth"), blank=False, null=True)
	phone_number = models.CharField(verbose_name=_("Phone Number"), blank=True, null=True, max_length = 13)
	role = models.CharField(max_length=50, choices=ROLE, blank= True, null = True)
	is_active = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	USERNAME_FIELD = 'username'

	def __str__(self):
		return self.username

	def clean(self, *args, **kwargs):
		phone_number = str(self.phone_number)
		if len(phone_number) < 4 or len(phone_number) > 10:
			raise ValidationError('In Phone Number minimum 7 length and maximum 13 is required')
		super(User, self).clean(*args, **kwargs)

	def save(self, *args, **kwargs):
		if not self.is_superuser:
			if self.role:
				self.role = "TEACHER"
			else:
				self.role = "STUDENT"
		super(User, self).save(*args, **kwargs)

