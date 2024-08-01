from django.urls import path
from .views import User

urlpatterns = [
    path('', User.as_view(), name='add_user')   # CRUD for User Operations
]