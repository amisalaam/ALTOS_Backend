from django.urls import path
from .views import EventListCreateAPIView, EventDetailAPIView, RegisterEventAPIView

urlpatterns = [
    # Event list and creation endpoint
    path('events/', EventListCreateAPIView.as_view(), name='events'),  # List all events or create a new event

    # Event detail, update, and delete endpoint
    path('events/<int:pk>/', EventDetailAPIView.as_view(), name='event_detail'),  # Retrieve, update, or delete a specific event by ID

    # Event registration endpoint
    path('register/event/', RegisterEventAPIView.as_view(), name='register_event'),  # Register a user for a specific event
]
