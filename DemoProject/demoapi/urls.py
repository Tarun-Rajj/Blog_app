from django.urls import path
from .views import *


urlpatterns = [
    path('first/',view_first_api)   #path : 127.0.0.1:8000/demoapi/first/
    
]
