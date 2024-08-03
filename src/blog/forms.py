from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
    widgets = {
        'title': forms.TextInput(attrs={'class':'form-control'}),
        'title_tag': forms.TextInput(attrs={'class':'form-control'}),
        'author': forms.TextInput(attrs={'class':'form-control'}),
        'body': forms.TextInput(attrs={'class':'form-control'}),
    }