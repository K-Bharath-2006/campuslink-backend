from django.urls import path
from .views import RegisterView, StudentLoginView, AdminLoginView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('student-login/', StudentLoginView.as_view()),
    path('admin-login/', AdminLoginView.as_view()),
]
