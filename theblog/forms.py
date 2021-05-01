from django import forms
from .models import *


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'title_tag', 'author', 'body')
		widgets = {
			'title' : forms.TextInput(attrs={'class': 'form-control'}),
			'title_tag' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'O texto que aparece na aba do navegador'}),
			'author' : forms.Select(attrs={'class': 'form-control'}),
			'body' : forms.Textarea(attrs={'class': 'form-control'}),
		}
		labels  = {
            'title':'Titulo',
            'title_tag':'Tag Titulo',
     		'author':'Escritor',
          	'body':'Texto',
        }
