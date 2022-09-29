from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from .models import Post
# Create your views here.


def post(request):
    
    
    return HttpResponse('message send successfully')
    



