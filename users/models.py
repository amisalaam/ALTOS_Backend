from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils import timezone
from datetime import timedelta

class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('You must have an email')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email=email, name=name, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.is_verified = True
        user.save()
        return user

    

class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()
 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']


    def __str__(self):
        return self.email
    


class OTP(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    otp = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def is_valid(self):
        return timezone.now() < self.created_at + timedelta(minutes=10)  # OTP valid for 10 minutes