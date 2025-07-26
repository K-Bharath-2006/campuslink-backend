from django.urls import path
from .views import get_announcements, create_announcement

urlpatterns = [
    path('', get_announcements, name='get_announcements'),
    path('create/', create_announcement, name='create_announcement'),
]
