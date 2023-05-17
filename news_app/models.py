from django.utils import timezone
from django.db import models
from django.db.models import DateTimeField



class PulishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=News.status.Pulished)
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name

class News(models.Model):

    class Status(models.TextChoices):
        Draft = 'DF', 'Draft'
        Pulished = 'PB', 'Pulished'


    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to='news/images')
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)
    publish_time = models.DateTimeField(default=timezone.now)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.Draft
                              )

    objects = models.Manager()
    published = PulishedManager()

    class Meta:
        ordering = ['-publish_time']

    def __str__(self):
        return self.title