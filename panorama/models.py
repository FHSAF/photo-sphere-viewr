from django.db import models

# Create your models here.

class Room(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    def __str__(self):
        return self.title

class ComponentImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.DO_NOTHING, related_name='component')
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    longitude = models.DecimalField(decimal_places=4, max_digits=4)
    latitude = models.DecimalField(decimal_places=4, max_digits=4)

    def __str__(self):
        return self.title
