from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['-name']


class Tag(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Tags'
        ordering = ['-name']


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s_related')
    tag = models.ManyToManyField(Tag, related_name='%(app_label)s_%(class)s_related')
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    content = RichTextUploadingField()
    is_active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

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


