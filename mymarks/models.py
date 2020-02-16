from django.db import models
from django.contrib.auth.models import User
import datetime


class mark(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(("Date"), default=datetime.date.today)
    subject = models.CharField(max_length=50)
    description = models.TextField()
    value = models.CharField(max_length=2)


class UserMeta(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    math = models.IntegerField(default=-1)
    russian = models.IntegerField(default=-1)
    chemistry = models.IntegerField(default=-1)
