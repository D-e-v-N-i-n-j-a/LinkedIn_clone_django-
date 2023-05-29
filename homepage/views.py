from django.shortcuts import render
from post.models import Post
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='accounts:login')
def homepage(request): 
    
    
    
    
    return render(request,'index.html',)

 
 