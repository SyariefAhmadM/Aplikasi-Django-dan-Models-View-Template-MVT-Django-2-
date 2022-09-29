from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField(null=True)
    is_finished = models.BooleanField(default = False)

