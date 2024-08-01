
from rest_framework import serializers
from .models import UserAccount, OTP
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import UserAccount
import random

class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['email', 'name', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserAccount.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        # Generate OTP
        otp = random.randint(100000, 999999)
        OTP.objects.create(user=user, otp=otp)

        # Send OTP email
        send_mail(
            'Your OTP Code',
            f'Your OTP code is {otp}',
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
        )

        return user




class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'), email=email, password=password)

            if not user:
                raise serializers.ValidationError('Invalid login credentials.')

            if not user.is_active:
                raise serializers.ValidationError('User account is disabled.')

            data['user'] = user
        else:
            raise serializers.ValidationError('Must include "email" and "password".')

        return data

    def create(self, validated_data):
        user = validated_data['user']
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': {
                'email': user.email,
                'name': user.name,
                'is_superuser': user.is_superuser  
            }
        }