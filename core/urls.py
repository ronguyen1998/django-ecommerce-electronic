from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from core.views.admin import view_admin
from core.views.detail import view_detail
from core.views.home import view_home
from core.views.auth import view_auth

urlpatterns = [ 
    path('', view_home.HomeView.as_view(), name='home'),
    path('login/',view_auth.LoginView.as_view(), name='login')

] + (
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        )