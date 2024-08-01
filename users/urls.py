from django.urls import path
from .views import UserRegistrationAPIView, OTPVerificationAPIView,LoginAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', UserRegistrationAPIView.as_view(), name='register'),
    path('api/otp/verify/', OTPVerificationAPIView.as_view(), name='otp_verify'),
      path('api/login/', LoginAPIView.as_view(), name='login'),
    
]