from django.db import models
from modules.teacher.models import Teacher
from django.utils.translation import ugettext_lazy as _
# Create your models here.
class Ratings(models.Model):
	GIVEN_BY = (
		("USER", 'User'),
		("TEACHER", 'Teacher')
	)
	class Meta:
		verbose_name = "Rating"
		verbose_name_plural = "Ratings"
	teacher = models.ForeignKey(Teacher, verbose_name=_('Teacher'), related_name="teacher_rating", blank=False, null=True, on_delete=models.CASCADE)
	user = models.ForeignKey(to="users.User", verbose_name=_('Student'), related_name="user_rating", null=False,on_delete=models.CASCADE)
	rating = models.FloatField(verbose_name=_('Rating'), null=True, blank=True, default=0)
	comment = models.TextField(verbose_name=_('Comment'), blank=True, null=False)
	given_by = models.CharField(max_length=50, default="", choices=GIVEN_BY)
	is_verified = models.BooleanField(verbose_name=_('Is Verified'), default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


	def __str__(self):
		return str(self.id)



class Instrument(models.Model):
	name = models.CharField(verbose_name=_("Name"), max_length=100, blank=False, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


class Specializations(models.Model):
	teacher = models.ForeignKey(Teacher, verbose_name=("Teacher"), on_delete=models.CASCADE, blank=False, null=True)
	instrument = models.ForeignKey(Instrument, verbose_name=("Instrument"), on_delete=models.CASCADE, blank=False, null=True)
	experience = models.FloatField(verbose_name=("Experience in Years"), blank=False, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)



class TeacherDocument(models.Model):
	teacher = models.ForeignKey(Teacher, verbose_name=("Teacher"), on_delete=models.CASCADE, blank=False, null=True)
	certificate = models.FileField(verbose_name='Certificate Record', blank=True, null=True, upload_to='teacher_document', default=('/dummy.png'))
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class MusicGenre(models.Model):
	class Meta:
		verbose_name = _("Music Genre")
		verbose_name_plural = _("Music Genres")

	name = models.CharField(verbose_name=_("Name"), max_length=100, blank=False, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


class StaticPages(models.Model):
	class Meta:
		verbose_name = _("Static page")
		verbose_name_plural = _("Static pages")

	ABOUT_US = "ABOUT US"
	CONTACT_US = "CONTACT US"
	TERMS_AND_CONDITIONS = "TERMS AND CONDITIONS"
	PRIVACY = "PRIVACY"
	HELP = "HELP"
	FAQs = "FAQs"

	TEMPLATE_TYPE = (
		(ABOUT_US, "About us"),
		(CONTACT_US, "Contact us"), 
		(TERMS_AND_CONDITIONS, "Terms & conditions"), 
		(PRIVACY, "Privacy"), 
		(HELP, "Help"),
		(FAQs, "FAQs")
	)

	template_name = models.CharField(max_length=50, choices = TEMPLATE_TYPE, unique=True)
	short_description = models.TextField()
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.template_name)
