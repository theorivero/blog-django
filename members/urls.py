from django.urls import path
from .views import *


urlpatterns = [
	path('register/', UserRegisterView.as_view(), name='register'),
	path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
	path('password/', PasswordsChangeView.as_view()),
	path('password/success', PasswordSuccess, name= 'success')

]
    