from rest_framework import serializers

from django.contrib.auth.models import User
from blog.models import Category, Tag, Series, NormalPost, SubPost


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'username')
        model = User


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name')
        model = Tag


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
    tag = TagSerializer(many=True)

    class Meta:
        fields = ('id', 'title', 'description', 'slug', 'content', 'published', 'created', 'updated',
                  'author', 'category', 'tag')
        model = NormalPost


class SubPostSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    series = SeriesSerializer()
    tag = TagSerializer(many=True)

    class Meta:
        fields = ('id', 'title', 'description', 'slug', 'content', 'published', 'created', 'updated',
                  'index', 'author', 'series', 'tag')
        model = SubPost

