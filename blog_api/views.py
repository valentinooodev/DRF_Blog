from django.http import Http404
from rest_framework import status, viewsets, permissions, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User

from blog.models import Category, Series, NormalPost, SubPost
from .serializers import CategorySerializer, SeriesSerializer, NormalPostSerializer, SubPostSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SeriesViewSet(viewsets.ModelViewSet):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer


class NormalPostViewSet(viewsets.ModelViewSet):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    queryset = NormalPost.objects.filter(is_active=True)
    serializer_class = NormalPostSerializer


class SubPostViewSet(viewsets.ModelViewSet):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    queryset = SubPost.objects.filter(is_active=True)
    serializer_class = SubPostSerializer


