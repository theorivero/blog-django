from django import forms
from .models import *

choices = Category.objects.all().values_list('name', 'name')
choice_list = [item for item in choices]




class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'title_tag','snippet', 'author', 'category', 'body',)
		widgets = {
			'title' : forms.TextInput(attrs={'class': 'form-control'}),
			'title_tag' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'O texto que aparece na aba do navegador'}),
			'snippet' : forms.Textarea(attrs={'class': 'form-control', 'rows':'3'}),
			'author' : forms.TextInput(attrs={'class': 'form-control', 'id': 'author', 'type': 'hidden'}),
			#'author' : forms.Select(attrs={'class': 'form-control'}),
			'category' : forms.Select(choices=Category.objects.all().values_list('name', 'name'),attrs={'class': 'form-control'}),
			'body' : forms.Textarea(attrs={'class': 'form-control'}),
		}
		labels  = {
            'title':'Titulo',
            'title_tag':'Tag Titulo',
            'snippet': 'Chamada',
     		'author':'Escritor',
     		'category':'Assunto',
          	'body':'Texto',

        }

class EditPostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'title_tag','snippet', 'body')
		widgets = {
			'title' : forms.TextInput(attrs={'class': 'form-control'}),
			'snippet' : forms.Textarea(attrs={'class': 'form-control', 'rows':'3'}),
			'title_tag' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'O texto que aparece na aba do navegador'}),
			'body' : forms.Textarea(attrs={'class': 'form-control'}),
		}
		labels  = {
            'title':'Titulo',
            'title_tag':'Tag Titulo',
            'snippet': 'Chamada',
          	'body':'Texto',
        }
