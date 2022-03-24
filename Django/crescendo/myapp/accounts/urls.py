from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.signup, name='signup'),
    path('password/', views.update_password, name='password'),
]
