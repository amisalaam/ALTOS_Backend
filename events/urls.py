
from django.urls import path
from .views import EventListCreateAPIView, EventDetailAPIView,RegisterEventAPIView

urlpatterns = [
 
    path('events/', EventListCreateAPIView.as_view(), name='events'),
    path('events/<int:pk>/', EventDetailAPIView.as_view(), name='events'),
    path('register/event/', RegisterEventAPIView.as_view(), name='register_event'),
]