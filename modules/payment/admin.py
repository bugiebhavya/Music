from django.contrib import admin
from .models import PaymentHistory
# Register your models here.
class PaymentHistoryAdmin(admin.ModelAdmin):
	list_display=['booking', 'transaction_id', 'amount', 'created_at']
	def has_add_permission(self, obj):
		return False

admin.site.register(PaymentHistory, PaymentHistoryAdmin)