from rest_framework import serializers

from django.contrib.auth.models import User
from blog.models import Category, Series, NormalPost, SubPost


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'username')
        model = User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'name', 'slug']
        model = Category


class SeriesSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        fields = ('id', 'title', 'slug', 'created', 'updated', 'category')
        model = Series


class NormalPostSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    category = CategorySerializer()

    class Meta:
        fields = ('id', 'title', 'description', 'slug', 'content', 'published', 'is_active', 'created', 'updated',
                  'author', 'category')
        model = NormalPost


class SubPostSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    series = SeriesSerializer()

    class Meta:
        fields = ('id', 'title', 'description', 'slug', 'content', 'published', 'is_active', 'created', 'updated',
                  'index', 'author', 'series')
        model = SubPost

