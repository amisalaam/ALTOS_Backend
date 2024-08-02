from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Event, UserEventRegistration
from .serializers import EventSerializer, RegistrationSerializer
from django.core.mail import send_mail
from django.conf import settings
from users.models import UserAccount



class EventListCreateAPIView(APIView):
    def get(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class EventDetailAPIView(APIView):
    def get(self, request, pk):
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
    
    def get(self, request,):
        email = request.query_params.get('email')
        if not email:
            return Response({"detail": "Email parameter is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = UserAccount.objects.get(email=email)
        except UserAccount.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        registrations = UserEventRegistration.objects.filter(user=user)
        events = [registration.event for registration in registrations]
        serializer = EventSerializer(events, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            event_id = serializer.validated_data['event_id']
            email = serializer.validated_data['email']
            user = UserAccount.objects.get(email=email)  # Fetch the user based on email

            try:
                event = Event.objects.get(id=event_id)
            except Event.DoesNotExist:
                return Response({"detail": "Event not found."}, status=status.HTTP_404_NOT_FOUND)

            if event.capacity <= 0:
                return Response({"detail": "Event capacity is full."}, status=status.HTTP_400_BAD_REQUEST)

            # Check if the user is already registered
            if UserEventRegistration.objects.filter(user=user, event=event).exists():
                return Response({"detail": "You are already registered for this event."}, status=status.HTTP_400_BAD_REQUEST)

            # Reduce capacity
            event.capacity -= 1
            event.save()

            # Save registration
            UserEventRegistration.objects.create(user=user, event=event)

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

    
