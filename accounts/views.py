from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.



def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            # print(email)
            print(password)
            messages.info(request,'Wrong credentials')
            return redirect('accounts:login')
    
    return render(request,'login.html')




def register(request):
    if request.method =='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        password2 = request.POST['password2']
        
        email_exist = User.objects.filter(email=email).exists()
        password_does_not_match = (password != password2)
        
        if email_exist:
            messages.info(request,'Email already exist')
            return redirect('register')
        
        elif password_does_not_match:
            messages.info(request,'password does not match')
            return redirect('register')
        else:
            user = User.objects.create_user(username=username,email=email,password=password)
            user.save()
            print('user created successfully')
            return redirect('login')
            
        
        
        
        
    
    return render(request,'registration.html')





def logout(request):
    auth.logout(request)
    print('user successfully logout')
    return redirect('accounts:login')