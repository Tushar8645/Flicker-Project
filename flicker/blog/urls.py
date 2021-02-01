from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.BlogView.as_view(), name='main_blog'),
    path('article/<int:pk>/', views.ArticleDetailView.as_view(),
         name='article_detail'),
    path('add_post/', views.AddPostView.as_view(), name='add_post'),
]
