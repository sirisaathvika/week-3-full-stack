from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('verify/<str:token>/', views.verify, name='verify'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
