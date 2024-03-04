from django.contrib import admin

from .models import Author, Category, Tag, Post, Keyword, SearchResult

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Keyword)
admin.site.register(SearchResult)
