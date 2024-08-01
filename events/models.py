from django.db import models
from users.models import UserAccount 

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    date = models.DateTimeField()
    capacity = models.IntegerField()

    def __str__(self):
        return self.title



class UserEventRegistration(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'event')

    def __str__(self):
        return f'{self.user.email} registered for {self.event.title}'
