from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts', views.posts, name='posts'),
    path('post/new', views.create_post, name='new-post'),
    path('post/<str:slug>', views.post, name='post')
]
