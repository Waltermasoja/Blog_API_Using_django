from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('get-all-posts/',views.getAllPosts),
    path('create-new-post/',views.CreatePost),
    path('delete-post',views.deletePost),
    path('get-post',views.getAllPosts),
    path('update-post',views.UpdatePost),
]