from django.shortcuts import render
from django.shortcuts import render
from django.views import generic
from .models import Post, Category
from .forms import PostForm, EditForm, CategoryForm
from django.urls import reverse_lazy


class BlogView(generic.ListView):
    model = Post
    template_name = 'blog/main_blog.html'
    ordering = ['-id']


def CategoryView(request, cats):
    category_post = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'blog/categories.html', {'cats': cats.title().replace('-', ' '), 'category_post': category_post})


class ArticleDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/article_detail.html'


class AddPostView(generic.CreateView):
    model = Post
    template_name = 'blog/add_post.html'
    form_class = PostForm


class AddCategoryView(generic.CreateView):
    model = Category
    template_name = 'blog/add_category.html'
    form_class = CategoryForm


class UpdatePostView(generic.UpdateView):
    model = Post
    template_name = 'blog/update_post.html'
    form_class = EditForm


class DeletePostView(generic.DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('blog:main_blog')
