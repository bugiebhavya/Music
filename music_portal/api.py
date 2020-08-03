from modules.booking.models import Booking
from django.db.models import Count
from modules.teacher.models import Teacher
from users.models import User
from django.db.models import Count
from modules.booking.models import Booking
from django.db.models.functions import ExtractWeekDay
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

@api.get("/dashboard_pie_chart")
def booking_pie_chart_count(request):
	query = Booking.objects.values('booking_status').annotate(count=Count('booking_status'))
	total_count = [{'name': booking.get('booking_status'), 'y': booking.get('count')} for booking in query.iterator()]
	return {"code": 200, "data": total_count}

@api.get('/dashboard_line_chart')
def booking_line_chart_count(request):
	query = Booking.objects.annotate(weekday=ExtractWeekDay('created_at')).values('weekday').annotate(
		count=Count('id')).values('weekday', 'count')
	weeks = [0 for i in range(7)]
	for booking in query.iterator():
		weeks[booking.get('weekday')-1] = booking.get('count')
	return {"code": 200, "data": weeks}

@api.get('dashboard_bargraph')
def booking_graph_view(request):
	query = (Booking.objects.all().extra(
		select={'month': "EXTRACT(month FROM created_at)", 'year': "EXTRACT(year FROM created_at)"}).values('month',
																											'year').annotate(
		count_items=Count('created_at'))).order_by('month')
	months = [0 for i in range(12)]
	for i in query.iterator():
		months[int(i.get('month')) - 1] = i.get('count_items')
	return {"code": 200, "data":months}
