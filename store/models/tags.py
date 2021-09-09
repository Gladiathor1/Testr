from django.db import models
from .subject import Subject
from .topic import Topic

class Tags(models.Model):
   subject_id = models.ForeignKey(Subject,on_delete=models.CASCADE,null=True,blank=True)
   topic_id = models.ForeignKey(Topic,on_delete=models.CASCADE,null=True,blank=True)


   def __str__(self):
      return '{} , {}'.format(self.subject_id, self.topic_id)
