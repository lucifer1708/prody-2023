from . import views
from django.urls import path

urlpatterns = [
    path('', views.EventList.as_view(), name='event_page'),
]
