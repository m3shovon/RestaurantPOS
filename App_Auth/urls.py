from django.urls import path
from . import views

app_name = 'App_Auth'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.admin_login_view, name='admin-login'),
     path('logout/', views.admin_logout_view, name='admin-logout'),
    
]


