from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Q # For complex look ups of the database 


class PostsQuerySet(models.QuerySet):
    def published(self):
        now=timezone.now()
        return self.filter(publish_date__lte=now)
    
    def search(self,query):
        lookup = (
            Q(title__icontains = query)|
            Q(content__icontains = query)|
            Q(slug__icontains = query)|
            Q(user__first_name__icontains = query)|
            Q(user__last_name__icontains = query)|
            Q(user__username__icontains = query)
        )
        return self.filter(lookup)


class PostsManager(models.Manager):
        def get_queryset(self):
            return PostsQuerySet(self.model , using=self._db)
        
        def published(self):
            return self.get_queryset().published()

        def search(self , query = None):
            if query is None:
                return self.get_queryset().none()
            return self.get_queryset().published().search(query)

class Posts(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , default = 1)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'media' , blank = True , null = True)
    slug = models.SlugField(unique = True )
    content = models.TextField(null=True , blank = True)
    publish_date = models.DateTimeField(auto_now=False , auto_now_add=False, null=True , blank = True)
    timestamp = models.DateTimeField( auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects=PostsManager()
    class Meta:
        ordering = ['-publish_date' , '-updated' , '-timestamp']


    def __str__(self):
        return self.title

