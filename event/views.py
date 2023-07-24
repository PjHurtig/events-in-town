from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Post
from .forms import EventForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(
        status=1, event_status='initial').order_by('event_start')
    template_name = 'index.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        for post in context['object_list']:
            post.update_event_status()

        context['last_event_added'] = Post.objects.filter(
            status=1).order_by('-created_on').first()
        context['last_event_start'] = Post.objects.filter(
            event_status='initial').order_by('event_start').first()
        return context

# initial code info for the "get_queryset" from
# https://stackoverflow.com/questions/6262629/sorting-through-request-get-in-django
# get_context_data info from_
# https://stackoverflow.com/a/36950584


class SortedPosts(generic.ListView):
    model = Post
    template_name = 'sorted_posts.html'
    paginate_by = 6

    def get_queryset(self):
        sort_by = self.request.GET.get('sort_by', '-created_on')

        if sort_by not in ['event_start',
                           '-event_start',
                           'created_on',
                           '-created_on']:
            sort_by = '-created_on'

        queryset = Post.objects.filter(
            status=1, event_status__in=['initial', 'cancelled'])

        if sort_by == 'event_start':
            queryset = queryset.order_by('event_start')
        elif sort_by == '-event_start':
            queryset = queryset.order_by('-event_start')
        elif sort_by == 'created_on':
            queryset = queryset.order_by('created_on')
        elif sort_by == '-created_on':
            queryset = queryset.order_by('-created_on')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        for post in context['object_list']:
            post.update_event_status()

        context['sort_by'] = self.request.GET.get('sort_by', '-created_on')
        context['post.event_start'] = Post.objects.filter(
            status=1, event_status__in=['initial', 'cancelled']).order_by(
                '-event_start').first()
        return context


class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        event_review_list = Review.objects.filter(event=post)
        sum = 0
        for review in event_review_list:
            sum += review.review
        review_score = sum/len(event_review_list)
        try:
            user_review = Review.objects.get(author=request.user)
            review_form = ReviewForm(initial={'review': user_review.review})
        except Review.DoesNotExist:
            review_form = ReviewForm()
        return render(
            request,
            'post_detail.html',
            {
                'post': post,
                'review_form': review_form,
                'review_score': review_score
            },
        )

    def post(self, request, slug, *args, **kwargs):
        review_starts = request.POST.get('review', 1)
        queryset = Post.objects.filter(status=1)
        event = get_object_or_404(queryset, slug=slug)
        author = request.user
        try:
            user_review = Review.objects.get(author=request.user)
            user_review.review = review_starts
            user_review.save()
            review_form = ReviewForm(initial={'review': user_review.review})
        except Review.DoesNotExist:
            review = Review(author=author, event=event, review=review_starts)
            review.save()
            review_form = ReviewForm(initial={'review': review.review})
            event_review_list = Review.objects.filter(event=event)
            sum = 0
            for review in event_review_list:
                sum += review.review
            review_score = sum/len(event_review_list)
        return render(
            request,
            'post_detail.html',
            {
                'post': event,
                'review_form': review_form,
                'review_score': review_score
            },
        )


class AddEvent(generic.CreateView):
    form_class = EventForm
    template_name = 'add_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Event Suceessfully Submitted!')
        return super().form_valid(form)


class MyEvents(generic.ListView):
    model = Post
    template_name = 'my_posts.html'
    paginate_by = 3

    def get_queryset(self):

        return Post.objects.filter(author=self.request.user)


class UpdateEvent(generic.UpdateView):
    model = Post
    form_class = EventForm
    template_name = 'update_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Event suceessfully Updated!')
        return super().form_valid(form)


class DeleteEvent(generic.DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('my_posts')

    def dispatch(self, request, *args, **kwargs):
        post = self.get_object()
        if not request.user.is_authenticated or post.author != request.user:
            messages.error(
                request, "You do not have permission to delete this post.")
            return redirect('my_posts')
        return super().dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Post deleted successfully.")
        return super().delete(request, *args, **kwargs)
