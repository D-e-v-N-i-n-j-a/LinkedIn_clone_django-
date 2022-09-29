from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    pic = models.ImageField(upload_to='pic')
    date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return f'user: {self.user.username}'
    
    






