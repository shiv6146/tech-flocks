from django.contrib.auth.models import User
from django import forms
from blog.models import Post
import lxml.html

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class PostForm(forms.ModelForm):
    url = forms.URLField()
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Post
        fields = ('url',)