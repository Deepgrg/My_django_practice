from django.shortcuts import render , get_object_or_404 , redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from .models import Posts
from .form import PostsModelForm


def blog_post_list_view(request):
    # List out objects
    # Could be search
    qs = Posts.objects.all() # query set -> list of python objects 
    context ={
        'object_list' : qs,
    }
    return render(request , "posts/blog_post_list_view.html" , context)

@login_required
def blog_post_create_view(request):
    form = PostsModelForm(request.POST or None)
    if form.is_valid():
        obj=form.save(commit = False)
        obj.user = request.user
        obj.save()
        return redirect('posts-list')
    context = {
        'form':form,
    }
    return render(request , 'posts/form.html' , context)


def blog_post_detail_view(request, slug):
    the_post = get_object_or_404(Posts , slug=slug)
    context ={
        "object" : the_post
    }
    return render(request , "posts/blog_post_detail_view.html" , context)

@login_required
def blog_post_update_view(request , slug):
    obj = get_object_or_404(Posts , slug = slug )
    form = PostsModelForm(request.POST or None , instance = obj)
    if form.is_valid():
        form.save()
        return redirect("posts-detail",slug=obj.slug)
    context = {
        "form" : form,
        "title" : f"Update {obj.title}",
    }
    return render(request , 'posts/blog_post_update_view.html' , context)

@login_required
def blog_post_delete_view(request , slug ):
    obj = get_object_or_404(Posts , slug = slug)
    if request.method =="POST":
        obj.delete()
        return redirect("posts-list")
    context = {
        "object" : obj,
    }
    return render(request , 'posts/blog_post_delete_view.html' , context)