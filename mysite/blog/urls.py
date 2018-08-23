from django.urls import path
from blog.views import PostListView, PostView

urlpatterns = [
        path('', PostListView.as_view(), name='post_list'),
        path('posts/<int:pk>/', PostView.as_view(), name='post_view'),
        ]