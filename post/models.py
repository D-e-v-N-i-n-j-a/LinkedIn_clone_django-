from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.TextField()
    image = models.ImageField(upload_to='post')
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'user :{self.user.username}: post:{self.title}'
    
    
    
    
    
    
    
    











