from django.shortcuts import render

from .models import SearchQuery
from posts.models import Posts

def search_view(request):
    query = request.GET.get('q' , None)
    user = None
    if request.user.is_authenticated:
        user = request.user
    context = { 'query' : query }
    if query is not None:
        SearchQuery.objects.create(user=user , query = query)
        posts_list = Posts.objects.search(query)
        context ['posts_list'] = posts_list
    return render(request,'searches/search_view.html', context)