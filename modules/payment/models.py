from django.db import models
from modules.booking.models import Booking
from django.utils.translation import ugettext_lazy as _
from django.contrib.postgres.fields import JSONField
# Create your models here.
class PaymentHistory(models.Model):

	class Meta:
		ordering = ['created_at']
		verbose_name = _('Payment History')
		verbose_name_plural = _('Payment history')

	TRANSACTION_STATUS = (
		("Pending", "Pending"),
		("Failed", "Failed"),
		("Complete", "Complete"))

	booking = models.ForeignKey(Booking, null=True, on_delete=models.CASCADE)
	status = models.CharField(max_length=20,choices=TRANSACTION_STATUS,help_text='Status da transação.')
	payment_response = JSONField(default=dict)
	transaction_id = models.CharField(max_length=100, default="", blank=True)
	amount = models.FloatField(default=0, verbose_name=_('Amount'))
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.id)