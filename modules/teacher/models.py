from django.db import models
from django.utils.translation import ugettext_lazy as _
from users.models import User
# from modules.configurations.models import MusicGenre
import pytz
# Create your models here.

# to = "users.User"

class Teacher(User):
	class Meta:
		verbose_name =_("Teacher")
		verbose_name_plural = _("Teachers")

	TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

	GENDER_CHOICES = (
		('MALE', 'Male'),
		('FEMALE', 'Female')
	)
	LEVEL_CHOICES = (
		('BEGINNER', 'Beginner'),
		('INTERMEDIATE', 'Intermediate'),
		('ADVANCED', 'Advanced')
	)

	profile_image = models.ImageField(verbose_name=_("Profile Image"), blank=True, null=True, upload_to="teacher_image", default="/dummy.png")
	gender = models.CharField(verbose_name=_("Gender"), choices=GENDER_CHOICES, blank=True, null=True, max_length=100)
	level = models.CharField(verbose_name=_("Level Taught"), choices=LEVEL_CHOICES, blank=True, null=True, max_length=100)
	country = models.CharField(verbose_name=_("Country"), max_length=30, blank=True, null=True)
	city = models.CharField(verbose_name=_("City"), max_length=50, blank=True, null=True)
	experience = models.FloatField(verbose_name=("Total Experience"), blank=True, null=True)
	time_zone = models.CharField(max_length=32, choices=TIMEZONES, blank=True, null=True, default='UTC')
	language = models.CharField(verbose_name=_("Language"), max_length=30, blank=True, null=True)
	video_file= models.FileField(verbose_name=_("Teacher Video"), upload_to="teacher_video", blank=True, null=True)
	short_introduction = models.TextField(verbose_name=("Teacher Introduction"), blank=True, null=True)
	about = models.TextField(verbose_name=("About Me"), blank=True, null=True)
	is_verified = models.BooleanField(verbose_name=("Is Verified ?"), default=False)
	music_genre = models.ManyToManyField(to="configurations.MusicGenre", verbose_name=_("MusicGenre"))

	def save(self, *args, **kwargs):
		self.role = "TEACHER"
		super(Teacher, self).save(*args, **kwargs)


class TeacherDocument(models.Model):
	teacher = models.ForeignKey(Teacher, verbose_name=("Teacher"), on_delete=models.CASCADE, blank=False, null=True)
	certificate = models.FileField(verbose_name='Certificate Record', blank=True, null=True, upload_to='teacher_document', default=('/dummy.png'))
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)