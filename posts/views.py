from django.shortcuts import render , get_object_or_404
from django.http import Http404

from .models import Posts
from .form import PostsForm,PostsModelForm


def blog_post_list_view(request):
    # List out objects
    # Could be search
    qs = Posts.objects.all() # query set -> list of python objects 
    context ={
        'object_list' : qs,
    }
    return render(request , "posts/blog_post_list_view.html" , context)


def blog_post_create_view(request):
    # Create objects
    # Use forms ?
    form = PostsModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        form= PostsModelForm()
    context = {
        'form':form,
    }
    return render(request , 'posts/form.html' , context)


def blog_post_detail_view(request, slug):
    # 1 object -> details
    obj = get_object_or_404(Posts , slug = slug)
    context = {
        "object" : obj,
    }
    return render(request, "posts/blog_post_detail_view.html" , context)


def blog_post_update_view(slug , request):
    obj = get_object_or_404(Posts , slug = slug)
    context = {
        "object" : obj,
    }
    return render(request , 'posts/blog_post_update_view.html' , context)


def blog_post_delete_view(slug , request):
    obj = get_object_or_404(Posts , slug = slug)
    context = {
        "object" : obj,
    }
    return render(request , 'posts/blog_post_delete_view.html' , context)