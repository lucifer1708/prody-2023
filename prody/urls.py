"""prody URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
# from django.views.generic.base import TemplateView
from events import views as user_views
from allauth.account.views import confirm_email
from django.conf.urls.static import static
from django.conf import settings
# from allauth.account.views import LoginView, SignupView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('accounts/', include('allauth.urls')),
    re_path(r'^rest-auth/registration/account-confirm-email/(?P<key>[-:\w]+)/$', confirm_email,
            name='account_confirm_email'),
    path('events/', include('events.urls')),
    path('sponsors/', user_views.SponsorsList.as_view(), name='sponsors'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
