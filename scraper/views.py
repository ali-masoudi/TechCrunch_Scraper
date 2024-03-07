from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Author, Category, Tag, Post, Keyword, SearchResult
from .serializers import AuthorSerializer, CategorySerializer, TagSerializer, PostSerializer, KeywordSerializer, \
    SearchResultSerializer
from .techcrunch_crawler import TechCrunchCrawler


class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class KeywordViewSet(viewsets.ModelViewSet):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer


class SearchResultViewSet(viewsets.ModelViewSet):
    queryset = SearchResult.objects.all()
    serializer_class = SearchResultSerializer


@api_view(['GET'])
def start(request):
    TechCrunchCrawler().get_posts()


@api_view(['POST'])
def search_post(request):
    query = request.data.get('query')
    if not query:
        return Response({"error": "Query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    TechCrunchCrawler().search_post(query)
    return Response({"message": "Search results saved successfully"}, status=status.HTTP_200_OK)
