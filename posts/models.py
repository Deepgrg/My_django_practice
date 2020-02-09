from django.db import models
from django.contrib.auth.models import User



class Posts(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , default = 1)
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique = True )
    content = models.TextField(null=True , blank = True)

    def __str__(self):
        return self.title

