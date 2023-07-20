from django.shortcuts import render
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1-3).order_by('event_date')
    template_name = 'index.html'
    paginate_by = 6
