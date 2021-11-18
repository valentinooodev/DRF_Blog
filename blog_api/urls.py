from django.urls import path, include
# from .views import CategoryViewSet, SeriesViewSet, NormalPostViewSet, SubPostViewSet
from rest_framework.routers import DefaultRouter
from .views import *

# router = DefaultRouter()
# router.register('categories', CategoryViewSet)
# router.register('series', SeriesViewSet)
# router.register('posts', NormalPostViewSet)
# router.register('sub-posts', SubPostViewSet)
#
app_name = 'blog_api'

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view()),
    path('categories/<int:pk>', CategoryDetailAPIView.as_view()),
    path('tags/', TagListAPIView.as_view()),
    path('posts/', NormalPostListAPIView.as_view()),
    path('posts/<int:pk>', NormalPostDetailAPIView.as_view()),
]
