from django.http import Http404
from rest_framework import status, viewsets, permissions, filters, generics
from rest_framework.response import Response
from commons.custom_pagination import CustomPagination

from blog.models import Category, Series, NormalPost, SubPost, Tag
from .serializers import CategorySerializer, SeriesSerializer, NormalPostSerializer, SubPostSerializer, TagSerializer


class CategoryListAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagListAPIView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class SeriesListAPIView(generics.ListCreateAPIView):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer


class SeriesDetailSerializer(generics.RetrieveUpdateDestroyAPIView):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer


class NormalPostListAPIView(generics.ListAPIView):
    queryset = NormalPost.objects.all()
    serializer_class = NormalPostSerializer
    pagination_class = CustomPagination

    def get(self, request, *args, **kwargs):
        category = request.GET.get('category') or ''
        if category == '':
            posts = NormalPost.objects.all()
        else:
            posts = NormalPost.objects.filter(category=category)
        serializer = NormalPostSerializer(posts, many=True)
        result = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(result)

