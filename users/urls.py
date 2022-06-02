from django.urls import path
from .views import ProfileView
from users.views import home

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('', home, name='home'),
]
