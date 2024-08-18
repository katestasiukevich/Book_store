from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from . import views

app_name = "accounts"

urlpatterns = [
    #path("login/", views.MyLoginView.as_view(), name="login"),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', views.CustomerProfileDetail.as_view(), name="profile"),
    path('profile-create/', views.CustomerProfileCreate.as_view(), name="profile-create"),
    path('register/', views.register, name='register'),
    #path('edit/', views.edit, name='edit'),
]
