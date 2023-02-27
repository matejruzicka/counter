from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView
from django.contrib.auth import views as authentication_views


from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('reset/<int:counter_id>', views.reset, name='reset'),
    path('delete/<int:counter_id>', views.delete, name='delete'),
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    path('login/', authentication_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', authentication_views.LogoutView.as_view(), name='logout'),
]
