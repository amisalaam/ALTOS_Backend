from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserRegistrationAPIView, OTPVerificationAPIView, LoginAPIView

urlpatterns = [
    # JWT token endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Endpoint to obtain a new token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Endpoint to refresh an existing token

    # User registration and authentication endpoints
    path('api/register/', UserRegistrationAPIView.as_view(), name='register'),  # Endpoint to register a new user
    path('api/otp/verify/', OTPVerificationAPIView.as_view(), name='otp_verify'),  # Endpoint to verify OTP during registration
    path('api/login/', LoginAPIView.as_view(), name='login'),  # Endpoint to login an existing user
]
