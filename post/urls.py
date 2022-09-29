from . import views
from django.urls import path



urlpatterns = [
        path('post',views.post,name='post'),
]








