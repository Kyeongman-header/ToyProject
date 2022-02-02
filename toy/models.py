from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.

class Image(models.Model):
    user=models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,)
    title = models.CharField(max_length=100)
    screenshot = models.ImageField(blank=True)
    pub_date=models.DateTimeField(default=timezone.localtime)

    def __str__(self):
        return str(self.title)

class Points(models.Model):
    user=models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,)
    point_one=models.FloatField(default=0, blank=True,null=True)
    point_two=models.FloatField(default=0,blank=True,null=True)
    point_three=models.FloatField(default=0,blank=True,null=True)
    pub_date=models.DateTimeField(default=timezone.localtime)

    def __str__(self):
        return str(self.title)
