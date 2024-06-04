from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=128, null=True, blank=True)
    par_1 = models.CharField(max_length=500, null=True, blank=True)
    par_2 = models.CharField(max_length=500, null=True, blank=True)
    par_3 = models.CharField(max_length=500, null=True, blank=True)
    par_4 = models.CharField(max_length=500, null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True)
    header_photo = models.CharField(max_length=500, null=True, blank=True)
    photo_1 = models.CharField(max_length=500, null=True, blank=True)
    photo_2 = models.CharField(max_length=500, null=True, blank=True)
    photo_3 = models.CharField(max_length=500, null=True, blank=True)
    photo_4 = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.title
    
