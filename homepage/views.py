from django.shortcuts import render
from post.models import Post
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def homepage(request):
    post = Post.objects.all().order_by('date')
    user = auth.get_user(request)
    if request.method == 'POST':
        title = request.POST['post']
        get_image = request.FILES['file']
        post_data = Post.objects.create(title=title,image = get_image,user =user)
        print('data saved successfully')
        post_data.save();
         
        return HttpResponseRedirect(request.path_info)
        
    
    
    return render(request,'index.html',{'data':post})

 
 