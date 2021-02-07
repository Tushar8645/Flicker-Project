import datetime

from django.contrib.auth.admin import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:main_blog')


class Post(models.Model):
    title = models.CharField(max_length=300)
    title_tag = models.CharField(max_length=300, default="")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=300, default="")

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        # return reverse('blog:article_detail', args=[str(self.id)])
        return reverse('blog:main_blog')
