from django.contrib import admin
from django.urls import path, include, re_path
from events import views as user_views
from allauth.account.views import confirm_email
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('accounts/', include('allauth.urls')),
    re_path(r'^rest-auth/registration/account-confirm-email/(?P<key>[-:\w]+)/$', confirm_email,
            name='account_confirm_email'),
    path('events/', include('events.urls')),
    path('sponsors/', user_views.SponsorsList.as_view(), name='sponsors'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
