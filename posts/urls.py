from django.urls import path
from . import views

urlpatterns = [
    path('' , views.blog_post_list_view , name ="posts-list"),
    path('<str:slug>/' , views.blog_post_detail_view , name ="posts-detail"),
    path('<str:slug>/update/' , views.blog_post_update_view , name ="posts-update"),
    path('<str:slug>/delete/' , views.blog_post_delete_view , name ="posts-delete"),
]