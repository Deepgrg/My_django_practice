from django.db import models

class Posts(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique = True )
    content = models.TextField(null=True , blank = True)


