from django.urls import path
from authentication_app import views
from django.contrib.auth import views as auth_views

app_name = 'authentication_app'

urlpatterns = [
    path('', views.sign_up, name='sign_up'),
    path('log_in/', views.log_in, name='log_in'),
    path('Log_out/', views.Log_out, name='Log_out'),

    #reset Password url start###########
    path('password_reset_email/', views.PasswordResetEmail, name='password_reset_email'),
    path('set_new_password/<user>/', views.SetNewPassword, name='set_new_password'),
    path('reset_password_valid_link/<uidb64>/<token>/', views.ResetPasswordValidLink, name='reset_password_valid_link'),
    #reset Password url start###########
    
    path('home/', views.Home, name='home'),
    
]