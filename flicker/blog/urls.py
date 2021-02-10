from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.BlogView.as_view(), name='main_blog'),
    path('article/<int:pk>/', views.ArticleDetailView.as_view(),
         name='article_detail'),
    path('add_post/', views.AddPostView.as_view(), name='add_post'),
    path('add_category/', views.AddCategoryView.as_view(), name='add_category'),
    path('article/edit/<int:pk>/',
         views.UpdatePostView.as_view(), name='update_post'),
    path('article/remove/<int:pk>/',
         views.DeletePostView.as_view(), name='delete_post'),
    path('category/<str:cats>/', views.CategoryView, name='category'),
]
