from django.db import models

class Papers_type(models.Model):
    paper_type = models.CharField(max_length=255)



    def __str__(self):
        return self.paper_type