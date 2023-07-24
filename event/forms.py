from .models import Post, Review
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
