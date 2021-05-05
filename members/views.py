from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from .forms import *
from django.contrib.auth import views as auth_views
from django.views.generic import ListView, DetailView, UpdateView
from theblog.models import Profile



class UserRegisterView(generic.CreateView):
	form_class = SignUpForm
	template_name = 'registration/register.html'
	success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
	form_class = EditProfileForm
	template_name = 'registration/edit_profile.html'
	success_url = reverse_lazy('home')

	def get_object(self):
		return self.request.user

class PasswordsChangeView(auth_views.PasswordChangeView):
	form_class = ChangePasswordForm
	template_name = 'registration/change-password.html'
	success_url = reverse_lazy('success')

def PasswordSuccess(request):
	return render(request, 'registration/password_success.html', {})

class ShowProfilePageView(DetailView):
	model = Profile
	template_name = 'registration/user_profile.html'

	def get_context_data(self, *args, **kwargs):
		#users = Profile.objects.all()
		context = super(ShowProfilePageView,self).get_context_data(*args, **kwargs)

		page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
		context['page_user'] = page_user
		return context

class EditProfilePageView(UpdateView):
	model = Profile
	template_name = 'registration/edit_profile_page.html'
	fields = ('bio', 'profile_pic', 'website_url', 'facebook_url', 'twitter_url', 'instagram_url')
	success_url = reverse_lazy('home')

