from rest_framework import serializers
from django.core.exceptions import ValidationError  
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class RegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    event_id = serializers.IntegerField()

    def validate(self, data):
        event = Event.objects.get(id=data['event_id'])
        if event.capacity <= 0:
            raise ValidationError("Event capacity is full.")
        return data