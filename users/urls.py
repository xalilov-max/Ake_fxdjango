from django.urls import path
from django.contrib.auth.views import (
    LoginView, 
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from .views import dashboard, register_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    
    # Password Reset URLs
    path('password-reset/', 
         PasswordResetView.as_view(template_name='users/password_reset.html'),
         name='password_reset'),
    path('password-reset/done/', 
         PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
]
