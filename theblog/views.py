from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from django.urls import reverse_lazy

#def home(request):
	#return render(request, 'home.html', {})

class HomeView(ListView):
	model = Post
	template_name = 'home.html'
	#ordering = ['-post_date']
	ordering = ['-id']


class ArticleDetailView(DetailView):
	model = Post
	template_name = 'article_details.html'

class AddPostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'add_post.html'
	#fields = '__all__'

class UpdatePostView(UpdateView):
	model = Post
	template_name = 'update_post.html'
	form_class = EditPostForm
	#fields = '__all__'

class DeletePostView(DeleteView):
	model = Post
	template_name = 'delete_post.html'
	success_url = reverse_lazy('home')

class AddCategoryView(CreateView):
	model = Category
	#form_class = CategoryForm
	template_name = 'add_category.html'
	fields = '__all__'
	#fields = '__all__'