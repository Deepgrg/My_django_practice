from django import forms
from .models import Posts


class PostsForm(forms.Form):
    title = forms.CharField(max_length = 100)
    slug = forms.SlugField()
    content = forms.CharField(widget = forms.Textarea)


class PostsModelForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields =['title' , 'slug' , 'content']

    def clean_title(self , *args , **kwargs):
        title = self.cleaned_data.get('title')
        qs = Posts.objects.filter(title__iexact = title)
        if qs.exists():
            raise forms.ValidationError ("This title is already used .Please choose another title")
        return title