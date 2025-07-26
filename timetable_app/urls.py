from django.urls import path
from . import views

urlpatterns = [
    path('timetable/', views.get_student_timetable),
    path('timetable/save/', views.save_or_update_timetable),
]
