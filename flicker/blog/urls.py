from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.BlogView.as_view(), name="MainBlog"),
    path('article/<int:pk>/', views.ArticleDetailView.as_view(), name='ArticleView'),
]
