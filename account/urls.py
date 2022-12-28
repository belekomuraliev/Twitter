from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', views.UserRegisterAPIView.as_view(), name='register'),
    path('token/', obtain_auth_token),
]
