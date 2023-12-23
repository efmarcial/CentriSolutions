from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin_page/', views.admin_page, name='admin_page'),
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
]
