from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _



class User(AbstractUser):
	class Meta:
		verbose_name =_("Student")
		verbose_name_plural = _("Students")

	username = models.CharField(verbose_name=_('Username'), max_length=100)
	email = models.EmailField(verbose_name=_('Email'),max_length=200,blank=False,null=False, unique=True)
	dob = models.DateField(verbose_name=_("Date of Birth"), blank=False, null=True)
	phone_number = models.IntegerField(verbose_name=_("Phone Number"), blank=True, null=True)
	is_active = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ('username',)

	def __str__(self):
		return self.username

	def clean(self, *args, **kwargs):
		phone_number = str(self.phone_number)
		if len(phone_number) < 4 or len(phone_number) > 10:
			raise ValidationError('In Phone Number minimum 7 length and maximum 13 is required')
		super(User, self).clean(*args, **kwargs)


