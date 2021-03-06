from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from core.views.admin import view_admin
from core.views.detail import view_detail
from core.views.home import view_home
from core.views.auth import view_auth

from core.views import views

urlpatterns = [     
    path('home', view_home.HomeView.as_view(), name='home'),
    # auth
    path('login/',view_auth.LoginView.as_view(), name='login'),
    path('sigup/',view_auth.SigupView.as_view(), name='sigup'),
    path('logout/', view_auth.Logout , name='logout'),

    # detail product
    path('detail/product/<int:id_product>',view_detail.DetailProductView,name='detail_product')

] + (
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        )