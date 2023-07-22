from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('sort/', views.SortedPosts.as_view(), name='sorted_posts.html'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
