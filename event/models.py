from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils import timezone

EVENT_TYPES = ((0, 'Music'), (1, 'Art'), (2, 'Other'))
STATUS = ((0, 'Draft'), (1, 'Published'), (2, 'Done'), (3, 'Cancelled'))
AREA_CHOICES = [
    ('jamtland', 'Jämtland'),
    ('ostersund', 'Östersund'),
    ('krokom', 'Krokom'),
    ('berg', 'Berg'),
    ('are', 'Åre'),
    ('bracke', 'Bräcke'),
    ('harjedalen', 'Härjedalen'),
    ('ragunda', 'Ragunda'),
    ('stromsund', 'Strömsund'),
]


# post model for ading events as posts
# initial code based on the django blog walkthrough project and adapted to
# fit this sites functions. Timezone import info from:
# https://docs.djangoproject.com/en/3.2/topics/i18n/timezones/
class Post(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    event_date = models.DateField(default=timezone.now)
    event_time = models.TimeField(default=timezone.now)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="event_posts")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    about = models.TextField()
    event_image = CloudinaryField('image', default='placeholder')
    link = models.URLField(blank=True)
    area = models.CharField(max_length=100, choices=AREA_CHOICES,
                            default='jamtland')
    locale = models.CharField(max_length=100)
    event_type = models.IntegerField(choices=EVENT_TYPES, default=0)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
