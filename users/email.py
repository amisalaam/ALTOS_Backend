from django.core.mail import send_mail

def send_activation_email(user):
    otp = 