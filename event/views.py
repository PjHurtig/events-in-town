from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post
from .forms import EventForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('event_start')
    template_name = 'index.html'
    paginate_by = 6


# initial code info for the "get_queryset" from
# https://stackoverflow.com/questions/6262629/sorting-through-request-get-in-django
class SortedPosts(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('created_on')
    template_name = 'sorted_posts.html'
    paginate_by = 6

    def get_queryset(self):
        sort_by = self.request.GET.get('sort_by', '-created_on')

        if sort_by not in ['event_start', 'event_type', 'created_on']:
            sort_by = '-created_on'

        return Post.objects.filter(status=1).order_by(sort_by)


class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            'post_detail.html',
            {
                'post': post,
            }
        )


class AddEvent(generic.CreateView):
    form_class = EventForm
    template_name = 'add_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
