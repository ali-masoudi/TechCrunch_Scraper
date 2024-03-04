from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, CategoryViewSet, TagViewSet, PostViewSet, KeywordViewSet, SearchResultViewSet,start

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'tags', TagViewSet)
router.register(r'posts', PostViewSet)
router.register(r'keywords', KeywordViewSet)
router.register(r'search-results', SearchResultViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('start/',start , name='start')
]
