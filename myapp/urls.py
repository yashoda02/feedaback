from django.urls import path
from .views import feedback_view, feedback_success, home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('feedback/', feedback_view, name='feedback_form'),
    path('success/', feedback_success, name='feedback_success'),
]
