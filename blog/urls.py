from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('export_posts_to_excel/', views.export_posts_to_excel, name='export_posts_to_excel'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('posts/new/', views.NewPost.as_view()),
    path('posts/<int:pk>/edit/', views.EditPost.as_view()),
]