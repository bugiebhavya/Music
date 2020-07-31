from django.db import models
from django.utils.translation import ugettext_lazy as _
from users.models import User
from modules.teacher.models import Teacher
from languages.fields import LanguageField
# Create your models here.


class Booking(models.Model):
	BOOKINGSTATUS = (
		# Self Cancel ?
		('PENDING', 'Pending'),
		('ACCEPT','Accept'),
		('REJECT','Reject'),
	)
	BOOKINGPAYMENTSTATUS = (
		("PENDING",'Pending'),
		("SUCCESS",'Success')
	)
	user = models.ForeignKey(User, verbose_name=('Student'), related_name="student", null=True,on_delete=models.CASCADE)
	teacher = models.ForeignKey(Teacher, verbose_name=_('Teacher'), null=True, on_delete=models.CASCADE)
	language = LanguageField(verbose_name=_("Language"), max_length=20) 
	date_of_upload = models.DateField(verbose_name=_("Video upload Date"))
	message = models.TextField(verbose_name=_('Message'))
	booking_status = models.CharField(verbose_name=_('Booking Status'), max_length=50, default='PENDING', choices=BOOKINGSTATUS)
	payment_status = models.CharField(verbose_name=_('Payment Status'), max_length=50, default="PENDING", choices=BOOKINGPAYMENTSTATUS)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)



class Media(models.Model):
	GIVEN_BY = (
		("USER", 'User'),
		("TEACHER", 'Teacher')
	)
	class Meta:
		verbose_name = "Media"
		verbose_name_plural = "Media"

	# booking
	booking = models.OneToOneField(Booking, verbose_name=_("Booking"), blank=False, null=True,on_delete=models.CASCADE)
	document = models.FileField(verbose_name=_("Teacher Document"))
	video_file= models.FileField(verbose_name=_("Teacher Video"), upload_to="teacher-videos", blank=True, null=True)
	description = models.TextField(verbose_name=_("Additional Information"), blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

