from django.shortcuts import render

from posts.models import Posts
from try_django.form import ContactForm

def home_page(request):
    qs = Posts.objects.all()[:4]
    context = {
        'title' : 'Welcome' ,
        'posts' : qs,
        }
       
    return render(request , 'blog/home_page.html' ,context)


def about_page(request):
    return render(request , 'blog/about_page.html' , {'title' : 'About'})


def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form=ContactForm()
    context ={
        'title' : 'Contact',
        'form' : form,
    }
    return render(request , 'blog/form.html' , context )