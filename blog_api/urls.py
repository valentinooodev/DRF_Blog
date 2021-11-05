from django.urls import path, include
from .views import CategoryViewSet, SeriesViewSet, NormalPostViewSet, SubPostViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('series', SeriesViewSet)
router.register('posts', NormalPostViewSet)
router.register('sub-posts', SubPostViewSet)

app_name = 'blog_api'

urlpatterns = [
    path('', include(router.urls)),
    # path('categories/', CategoryList.as_view()),
    # path('categories/<int:pk>', CategoryDetail.as_view()),
]