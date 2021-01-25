from django.shortcuts import render
from django.views import generic


class MainBlog(generic.TemplateView):
    template_name = 'blog/MainBlog.html'
