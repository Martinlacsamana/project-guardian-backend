from django.db import models

# This is like your schema in NodeJS
class User(models.Model):
    user_id: models.CharField(max_length=30, unique=True)
    phone_number: models.CharField(max_length=10)

def __str__(self):
    return self.user_id

