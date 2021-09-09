from django.db import models
from.papers import Paper
from .image import Image
from .answers import Answer
from .tags import Tags
from .discipline import Discipline

class Question(models.Model):

    MCQ = 'MCQ'
    Fill_in_the_blank = 'Fitb'
    Descriptive = 'Descriptive'

    Easy = 'Easy'
    Medium = 'Medium'
    Hard = 'Hard'
    diff = [
        (Easy, 'Easy'),
        (Medium, 'Medium'),
        (Hard, 'Hard')
    ]

    typ = [
        (MCQ,'MCQ'),
        (Fill_in_the_blank,'Fill in the blank'),
        (Descriptive,'Descriptive')
    ]

    difficulty = models.CharField(
        max_length=255,
        choices=diff,
        default=Descriptive,
    )
    type = models.CharField(max_length=25,choices=typ,default=None)
    created_time = models.DateTimeField(auto_now_add=(True))
    paper_id = models.ForeignKey(Paper, on_delete=models.CASCADE, null=True,blank=True)
    image_id = models.ForeignKey(Image,on_delete=models.CASCADE,null=True,blank=True)
    answer_id = models.ForeignKey(Answer,on_delete=models.CASCADE,null=True,blank=True)
    tag_id = models.ForeignKey(Tags,on_delete=models.CASCADE,null=True,blank=True)
    discipline_id = models.ForeignKey(Discipline,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return '{} , {} , {} , {}'.format(self.paper_id, self.difficulty, self.type, self.tag_id)
