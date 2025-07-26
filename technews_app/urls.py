from django.urls import path
from .views import get_technews, create_technews

urlpatterns = [
    path('technews/', get_technews),
    path('technews/create/', create_technews),
]
