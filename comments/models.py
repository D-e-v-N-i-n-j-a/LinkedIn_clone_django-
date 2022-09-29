from django.db import models
from post.models import Post
from django.contrib.auth.models import User
# Create your models here.

class Comments(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return f'user:{self.user.username}'



class CommentNotificationCounter(models.Model):
    count = models.IntegerField()
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    comment = models.ForeignKey(Comments,on_delete=models.CASCADE)
    is_viewed = models.BooleanField(default=False, blank=True)
    
    













