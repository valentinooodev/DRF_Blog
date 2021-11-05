from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['-name']


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s_related')
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published')
    content = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class Series(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Series'
        ordering = ['-updated']


class NormalPost(Post):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)

    class Meta:
        verbose_name_plural = 'Normal Posts'
        ordering = ['-updated']


class SubPost(Post):
    series = models.ForeignKey(Series, on_delete=models.CASCADE, related_name='blog_sub_post')
    index = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Sub Posts'
        ordering = ['-index']

