
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #Include created apps urls
    path('',include('users.urls')),
    path('api/',include('events.urls')),
]
