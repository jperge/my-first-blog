from django.conf import settings
from django.db import models
from django.utils import timezone
from django import forms



COLOR_CHOICES = (
    ('green','GREEN'),
    ('blue', 'BLUE'),
    ('red','RED'),
    ('orange','ORANGE'),
    ('black','BLACK'),
)


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text  = models.CharField(max_length=100, choices=COLOR_CHOICES, default='green')
    # text = forms.CharField(label='Pick a color', widget=forms.Select(choices=COLOR_CHOICES))
    #text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
