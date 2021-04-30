from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *


#def home(request):
	#return render(request, 'home.html', {})

class HomeView(ListView):
	model = Post
