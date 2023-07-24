from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django_extensions.db.fields import AutoSlugField
from django.utils import timezone
from django.urls import reverse


EVENT_TYPES = ((0, 'Music'), (1, 'Art'), (2, 'Other'))
STATUS = ((0, 'Draft'), (1, 'Published'))
EVENT_STATUS = [
    ('initial', 'Initial'),
    ('passed', 'Passed'),
    ('cancelled', 'Cancelled'),
]
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


REVIEW_TYPES = ((1, '1 Star'),
                (2, '2 Stars'),
                (3, '3 Stars'),
                (4, '4 Stars'),
                (5, '5 Stars'),
                )

# post model for ading events as posts
# initial code based on the django blog walkthrough project and adapted to
# fit this sites functions. Timezone import info from:
# slug from
# https://django-extensions.readthedocs.io/en/latest/field_extensions.html#
# https://docs.djangoproject.com/en/3.2/topics/i18n/timezones/


class Post(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    event_start = models.DateTimeField(default=timezone.now)
    slug = AutoSlugField(
        populate_from=['title', 'event_start'], max_length=200, unique=True)
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
    status = models.IntegerField(choices=STATUS, default=1)
    event_status = models.CharField(
        max_length=10, choices=EVENT_STATUS, default='initial')

    def is_event_cancelled(self):
        return self.event_status == 'cancelled'

    def is_event_passed(self):
        return self.event_start < timezone.now()

    def update_event_status(self):
        if self.is_event_passed():
            self.event_status = 'passed'
        elif self.is_event_cancelled():
            self.event_status = 'cancelled'
        else:
            self.event_status = 'initial'

        self.save()

    class Meta:
        ordering = ['-created_on']

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
