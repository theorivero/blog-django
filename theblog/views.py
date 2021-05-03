from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

#def home(request):
	#return render(request, 'home.html', {})

class HomeView(ListView):
	model = Post
	template_name = 'home.html'
	#ordering = ['-post_date']
	ordering = ['-id']
	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(HomeView,self).get_context_data(*args, **kwargs)
		context['cat_menu'] = cat_menu
		return context

#_-_-_-_-_-_-_-_-_-_-_-_-Posts-_-_-_-_-_-_-_-_-_-_-_-#

class ArticleDetailView(DetailView):
	model = Post
	template_name = 'article_details.html'
	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(ArticleDetailView,self).get_context_data(*args, **kwargs)
		post = get_object_or_404(Post, id=self.kwargs['pk'])

		liked = False
		if post.likes.filter(id=self.request.user.id).exists():
			liked = True
		
		context['liked'] = liked
		context['total_likes'] = post.total_likes()
		context['cat_menu'] = cat_menu
		return context


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

#_-_-_-_-_-_-_-_-_-_-_-_-Category_-_-_-_-_-_-_-_-_-_-_-_-#
class AddCategoryView(CreateView):
	model = Category
	#form_class = CategoryForm
	template_name = 'add_category.html'
	fields = '__all__'
	#fields = '__all__'

def CategoryView(request, cats):
	cats = cats.replace('-', ' ')
	category_posts = Post.objects.filter(category=cats)
	context =  {'category_posts':category_posts, 'cats':cats}


	return render(request, 'categories.html', context)


def CategoryListView(request):
	cat_menu_list = Category.objects.all()

	context =  {'cat_menu_list':cat_menu_list}

	return render(request, 'categories_list.html', context)

#_-_-_-_-_-_-_-_-_-_-_-_-Likes-_-_-_-_-_-_-_-_-_-_-_-#
def LikeView(request, pk):
	post = get_object_or_404(Post, id=request.POST.get('post_id'))
	liked=False
	if post.likes.filter(id=request.user.id).exists():
		post.likes.remove(request.user)
		liked = False
	else:
		post.likes.add(request.user)
		liked = True

	return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))
