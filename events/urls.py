from . import views
from django.urls import path
app_name = 'events'

urlpatterns = [
    path('', views.EventList.as_view(), name='event_page'),
    path('addevent/', views.event_reg, name='addevent'),
]
