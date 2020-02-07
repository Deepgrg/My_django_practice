from django.shortcuts import render

from try_django.form import ContactForm

def home_page(request):
    context = {
        'title' : 'Non user data' ,
         
        }
    if request.user.is_authenticated :
        context = {
        'title' : 'User data' ,
         'list' : [1,2,3,5,6,8],
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