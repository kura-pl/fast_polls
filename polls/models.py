from django.db import models

class Question(models.Model):
    title = models.CharField(max_length=100)
    question_text = models.CharField(max_length=300)
    pub_date = models.DateTimeField('Publication Date')

    def __str__(self):
        return self.title

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=300)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text