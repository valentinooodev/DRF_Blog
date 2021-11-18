from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Category, Tag, Series, NormalPost, SubPost


class NormalPostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = NormalPost
        fields = '__all__'


class SubPostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = SubPost
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    list_filter = ['is_active']


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ['category', 'title', 'slug', 'created', 'updated']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(NormalPost)
class NormalPostAdmin(admin.ModelAdmin):
    form = NormalPostForm
    list_display = ['author', 'category', 'title', 'is_active', 'created', 'updated']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['is_active', 'author', 'category']


@admin.register(SubPost)
class SubPostAdmin(admin.ModelAdmin):
    forms = SubPostForm
    list_display = ['author', 'series', 'title', 'index', 'is_active', 'created', 'updated']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['is_active', 'author', 'series']
