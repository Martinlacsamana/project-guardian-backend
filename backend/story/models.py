from django.db import models

class Story(models.Model):
    _id: models.CharField(max_length=30, unique=True)
    title: models.TextField()  
    text: models.TextField()
    location: models.CharField(max_length=30)
    image: models.CharField(max_length=60)
    user_id: models.CharField(max_length=30, unique=True)

# Our constructor whenever we want to print this object
def __str__(self):
    return f"ID is {self._id}. Title is {self.title}"



# TextField() is for unbounded values -> of course slower indexing