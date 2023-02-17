from django.db import models
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Modules(models.Model):
#      name=models.CharField(max_length=255)


class Todo(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    deadline=models.DateTimeField(auto_now_add=True)
    isCompleted=models.BooleanField(default=False)
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)




