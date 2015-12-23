from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=300)
    pub_date = models.DateTimeField('Data publikacji')
    authors_mail = models.CharField(max_length=100)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=300)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text