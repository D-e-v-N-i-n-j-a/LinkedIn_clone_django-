from . import views
from django.urls import path


urlpatterns = [
    path('post-comments',views.comments,name='comments'),
    path('getComments/<str:pk>/',views.allComments,name='getComments'),
]






