from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    # path('index/', views.index, name='index'),
    path('register/', views.RegisterView, name='register'),
    path('login/', views.LoginView, name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('forgot-password/', views.ForgotPassword, name='forgot-password'),
    # path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('password-reset-sent/<str:reset_id>/', views.PasswordResetSent, name='password-reset-sent'),
    path('reset-password/<str:reset_id>/', views.ResetPassword, name='reset-password'),
    path('travel-requests/', views.travel_requests, name='travel_requests'),
    path('payslip/', views.payslip, name='payslip'),
    path('user-management/', views.user_management, name='user_management'),
]