
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserAccountSerializer
from .models import UserAccount, OTP

# Create your views here.

class UserRegistrationAPIView(APIView):
    def post(self, request, *args, **kwargs):
        print(request  ,'bbbbbbbbbb')
        serializer = UserAccountSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'email': user.email,
                'name': user.name,
                'message': 'User registered successfully. Check your email for the OTP.'
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    