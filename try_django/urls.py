from django.contrib import admin
from django.urls import path,re_path,include
from posts import views as posts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('blog.urls')),
    path('post/newpost/' , posts_views.blog_post_create_view , name ="posts-create"),
    path('post/' , include('posts.urls')),
]
