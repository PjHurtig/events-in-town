from .models import Post
from django import forms


class EventForm(forms.ModelForm):
    '''create event form'''

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Post
        fields = [
            'title',
            'artist',
            'event_start',
            'about',
            'event_image',
            'link',
            'area',
            'locale',
            'event_type',
            'event_status',
        ]


class ReviewForm(forms.ModelForm):
    '''create review form'''

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Review
        fields = [
            'review',
        ]
