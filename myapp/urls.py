# myapp/urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import PostListAPIView, PostDetailAPIView

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/create/', views.post_create, name='post_create'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:post_id>/delete/', views.post_delete, name='post_delete'), 
    path('signup/', views.signup, name='signup'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/myapp/'), name='logout'),
    path('api/posts/', PostListAPIView.as_view(), name='api-post-list'),
    path('api/posts/<int:id>/', PostDetailAPIView.as_view(), name='api-post-detail'),

]
