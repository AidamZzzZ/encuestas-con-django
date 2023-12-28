from django.db import models
import datetime
from django.utils import timezone
from django.contrib import admin

#modelo de base de datos de preguntas
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateField("date published")
    
    def __str__(self):
        return self.question_text
    
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently",
    )

    def was_published_recently(self):
        now = timezone.now()
        return self.pub_date >= now.date() - datetime.timedelta(days=1)
    
#modelo de base de datos de elecciones
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text