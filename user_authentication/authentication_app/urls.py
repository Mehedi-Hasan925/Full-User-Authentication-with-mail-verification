from django.urls import path
from authentication_app import views

app_name = 'authentication_app'

urlpatterns = [
    path('', views.sign_up, name='sign_up'),
    path('log_in/', views.log_in, name='log_in'),
    path('Log_out/', views.Log_out, name='Log_out'),
    path('home/', views.Home, name='home'),
    path('activate/<uidb64>/<token>/', views.ActivateView.as_view(), name='activate'),
]