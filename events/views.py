from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Event
from .serializers import EventSerializer, RegistrationSerializer
from django.core.mail import send_mail
from django.conf import settings



class EventListCreateAPIView(APIView):
    def get(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request.data)
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class EventDetailAPIView(APIView):
    def get(self, request, pk):
        print(pk)
        event = get_object_or_404(Event, pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)
    
    def put(self, request, pk):
        event = get_object_or_404(Event, pk=pk)
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, pk):
        event = get_object_or_404(Event, pk=pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class RegisterEventAPIView(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data,'kkkkkkkk')
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            event_id = serializer.validated_data['event_id']
            email = serializer.validated_data['email']

            try:
                event = Event.objects.get(id=event_id)
            except Event.DoesNotExist:
                return Response({"detail": "Event not found."}, status=status.HTTP_404_NOT_FOUND)

            if event.capacity <= 0:
                return Response({"detail": "Event capacity is full."}, status=status.HTTP_400_BAD_REQUEST)

            # Reduce capacity
            event.capacity -= 1
            event.save()

            # Send confirmation email
            send_mail(
                'Event Registration Confirmation',
                f'You have successfully registered for the event "{event.title}".',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )

            return Response({"detail": "Registration successful."}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)