from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.api_testing, name='api_testing'),
]