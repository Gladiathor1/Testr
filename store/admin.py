from django.contrib import admin
from .models.papers import Paper
from .models.questions import Question
from .models.subject import Subject
from .models.discipline import Discipline
from .models.paper_type import Papers_type
from .models.answers import Answer
from .models.tags import Tags
from .models.topic import Topic
from  .models.image import Image


#class AdminPapers(admin.ModelAdmin):
 #   list_display =

# Register your models here.
admin.site.register(Question)
admin.site.register(Paper)
admin.site.register(Answer)
admin.site.register(Discipline)
admin.site.register(Image)
admin.site.register(Papers_type)
admin.site.register(Subject)
admin.site.register(Tags)
admin.site.register(Topic)