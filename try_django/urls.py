from django.contrib import admin
from django.urls import path,re_path,include
from posts import views as posts_views
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('blog.urls')),
    path('post/newpost/' , posts_views.blog_post_create_view , name ="posts-create"),
    path('post/' , include('posts.urls')),
]

if settings.DEBUG: 
    # This url pattern is to mimic the content delivery network (cdn) like AWS during the development mode
    
    # static_cdn = STATIC_ROOT
    # media_cdn = MEDAI_ROOT
    # settings.STATIC_URL = '/static/'
    # settings.MEDAI_URL = '/media/'


    from django.conf.urls.static import static

    # to copy files from static to static_cdn directory
    urlpatterns += static(settings.STATIC_URL , document_root = settings.STATIC_ROOT)

    # to copy files from media to media_cdn directory
    urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
    

