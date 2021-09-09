from django.db import models

class Discipline(models.Model):
    discipline = models.CharField(max_length=255)





    def __str__(self):
        return self.discipline