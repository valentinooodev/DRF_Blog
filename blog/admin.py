from django.contrib import admin

from .models import Category, Series, NormalPost, SubPost


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ['category', 'title', 'slug', 'created', 'updated']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(NormalPost)
class NormalPostAdmin(admin.ModelAdmin):
    list_display = ['author','category', 'title', 'is_active', 'created', 'updated']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['is_active', 'author', 'category']


@admin.register(SubPost)
class SubPostAdmin(admin.ModelAdmin):
    list_display = ['author', 'series','title','index', 'is_active', 'created', 'updated']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['is_active', 'author', 'series']
