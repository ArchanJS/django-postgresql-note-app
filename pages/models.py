from statistics import mode
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    postTitle=models.CharField(max_length=200)
    postedBy=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.CharField(max_length=1000)
    def __str__(self):
        return self.postTitle