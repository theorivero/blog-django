from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	title = models.CharField(max_length=255)
	title_tag = models.CharField(max_length=255, default='Blog!')
	author = models.ForeignKey(User, on_delete=models.CASCADE) #models.CASCADE caso o user seja apagado todos os seus posts são apagados tbm
	body = models.TextField()

	def __str__(self):
		return self.title + ' | ' + str(self.author)