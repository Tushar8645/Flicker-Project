from django.shortcuts import render
from django.views import generic
from .models import Post


class BlogView(generic.ListView):
    model = Post
    template_name = 'blog/MainBlog.html'


class ArticleDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/ArticleView.html'
