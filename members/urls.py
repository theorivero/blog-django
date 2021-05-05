from django.urls import path
from .views import *


urlpatterns = [
	path('register/', UserRegisterView.as_view(), name='register'),
	path('edit_settings/', UserEditView.as_view(), name='edit_profile'),
	path('password/', PasswordsChangeView.as_view()),
	path('password/success', PasswordSuccess, name= 'success'),
	path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='profile'),
	path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'),


]
    