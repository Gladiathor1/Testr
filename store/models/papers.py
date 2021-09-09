import datetime

from django.db import models
from.paper_type import Papers_type
from .subject import Subject
from .discipline import Discipline


class Paper(models.Model):
    Paper_no = models.IntegerField(default=0)
    date = models.DateField()
    paper_type_id = models.ForeignKey(Papers_type,on_delete=models.CASCADE,null=True,blank=True)
    subject_id = models.ForeignKey(Subject,on_delete=models.CASCADE,null=True,blank=True)
    discipline_id = models.ForeignKey(Discipline,on_delete=models.CASCADE,null=True,blank=True)
    doc = models.FileField(upload_to='uploads/papers', null=True,blank=True)

    def __str__(self):
        return '{} , {} , {} , {} , {}'.format(self.subject_id, self.paper_type_id, self.date, self.discipline_id, self.Paper_no)
