from django.urls import path
from .views import Story

urlpatterns = [
    path('', Story.as_view(), name="Story") # Will hold the CRUD operations for this
]