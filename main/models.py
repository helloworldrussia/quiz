from django.db import models


class Question(models.Model):
    cat_numb = models.IntegerField()
    price = models.IntegerField()
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=255)
    success_mess = models.CharField(max_length=255)
    fail_mess = models.CharField(max_length=255)

    def __str__(self):
        return self.question