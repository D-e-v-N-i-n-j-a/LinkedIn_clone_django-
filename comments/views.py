from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.contrib import auth
from post.models import Post
from .models import Comments
# Create your views here.


def comments(request):
    get_user = auth.get_user(request)
    get_post = Post.objects.get(id=int('1'))
    
    pass



def allComments(request,pk):
    list_comments = []
    get_by_post_id =Post.objects.get(id=pk)
    get_comments = Comments.objects.filter(post=get_by_post_id)
    for item in get_comments:
        data = {
            'comment':item.comment,
            'user':item.user.username,
            'user_profile':item.user.profile.pic.url,
            'post_id':item.post.id
            
        }
        list_comments.append(data)
        
    
    
    return JsonResponse({'data':list_comments})



