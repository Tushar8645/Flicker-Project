from django.shortcuts import render
from django.views import generic
from .models import Post


class BlogView(generic.ListView):
    model = Post
    template_name = 'blog/main_blog.html'


class ArticleDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/article_detail.html'

class AddPostView(generic.CreateView):
    model = Post
    template_name = 'blog/add_post.html'
    fields = '__all__'