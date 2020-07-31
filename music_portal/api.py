from modules.booking.models import Booking
from django.db.models import Count
from modules.teacher.models import Teacher
from users.models import User

from ninja import NinjaAPI
import pdb

api = NinjaAPI()


@api.get("/dashboard_count")
def dashboard_count(request):
	booking_count = Booking.objects.count()
	teacher_count = Teacher.objects.count()
	student_count = User.objects.filter(is_superuser=False).count()
	message = "Dashboard count fetched"
	return {"message":message, "code": 200, "data": {"booking_count":booking_count, "teacher_count": teacher_count, "student_count":student_count}, 'error_message':""}