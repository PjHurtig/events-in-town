from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('sort/', views.SortedPosts.as_view(), name='sorted_posts.html'),
    path('addpost/', views.AddEvent.as_view(), name='add_post'),
    path('myposts/', views.MyEvents.as_view(), name='my_posts'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('posts/<slug:slug>/update',
         views.UpdateEvent.as_view(), name='update_post'),
    path('posts/<slug:slug>/delete',
         views.DeleteEvent.as_view(), name='delete_post'),
]
