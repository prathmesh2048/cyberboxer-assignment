from django.db import models
from django.db.models.base import Model

class Images(models.Model):
    image_name = models.CharField(max_length=50, blank=True, default="None")
    image = models.FileField(upload_to='images',blank=True)
    date_posted = models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return self.image_name