# serializers.py
from rest_framework import serializers
from .models import UserAccount, OTP
from django.core.mail import send_mail
from django.conf import settings
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
