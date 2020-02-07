from django.urls import path
from . import views


urlpatterns = [
    path('',views.home_page , name="home-page"),
    path('contact/' , views.contact_page , name='contact-page'),
    path('about/' , views.about_page , name='about-page'),

]