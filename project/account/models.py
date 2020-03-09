from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Profile(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    rank=models.CharField(max_length=30,choices=(('ceo','CEO'),('cto','CTO'),('hr','HR'),('sd','Senior Devoler'),('jd','Junior Devolper')))
    def __str__(self):
        return self.rank
    
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField(default="")
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('home')
