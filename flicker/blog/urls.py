from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.MainBlog.as_view(), name="MainBlog")
]
