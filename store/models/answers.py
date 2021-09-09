from django.db import models
from .image import Image


class Answer(models.Model):
    Answer = models.TextField(null=True,blank=True)
    Image_id = models.ForeignKey(Image,on_delete=models.CASCADE,null=True,blank=True)