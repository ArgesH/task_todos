from django.db import models

# Create your models here.

class Photo(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos/')  # files go into MEDIA_ROOT/photos/ -> /media/photos/

    def __str__(self):
        return self.title

