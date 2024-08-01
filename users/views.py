
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserAccountSerializer, LoginSerializer
from .models import UserAccount, OTP

# Create your views here.

class UserRegistrationAPIView(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data ,'bbbbbbbbbb')
        serializer = UserAccountSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'email': user.email,
                'name': user.name,
                'message': 'User registered successfully. Check your email for the OTP.'
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class OTPVerificationAPIView(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data ,'cccccccccc')
        email = request.data.get('email')
        otp_code = request.data.get('otp')

        try:
            user = UserAccount.objects.get(email=email)
            otp = OTP.objects.get(user=user, otp=otp_code)

            if otp.is_valid():
                user.is_verified = True
                user.save()
                otp.delete()  # Remove OTP after successful verification
                return Response({'message': 'User verified successfully.'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'OTP has expired.'}, status=status.HTTP_400_BAD_REQUEST)

        except (UserAccount.DoesNotExist, OTP.DoesNotExist):
            return Response({'error': 'Invalid email or OTP.'}, status=status.HTTP_400_BAD_REQUEST)



class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            tokens = serializer.save()
            return Response(tokens, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
