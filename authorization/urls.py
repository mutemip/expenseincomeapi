from django.urls import path
from .views import (RegisterView, VerifyEmail, LoginAPIView, PasswordTokenCheckAPIView,
                    RequestPasswordResetAPIView, SetNewPasswordAPIView, LogoutAPIView)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('email-verify', VerifyEmail.as_view(), name='email-verify'),
    path('request-reset-email', RequestPasswordResetAPIView.as_view(), name='request-reset-email'),
    path('pasword-rest/<uidb64>/<token>/', PasswordTokenCheckAPIView.as_view(), name='pasword-rest-confirm'),
    path('password-reset-complete', SetNewPasswordAPIView.as_view(), name='password-reset-complete'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout', LogoutAPIView.as_view(), name='logout')
]
