from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta :
        model = Post
        fields=['title','image','title','description','published']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    class Meta :
        fields = ['username','password']
