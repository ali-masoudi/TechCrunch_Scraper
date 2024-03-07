from html import unescape
from urllib.parse import quote

import requests

from .models import *


class TechCrunchCrawler(object):
    def __init__(self, base_url='https://techcrunch.com',
                 main_api_route='wp-json/wp/v2',
                 author_route='users',
                 category_route='categories',
                 tag_route='tags',
                 post_route='posts',
                 search_route='search',
                 embed=False):
        self.base_url = base_url
        self.main_api_route = main_api_route
        self.author_route = author_route
        self.category_route = category_route
        self.tag_route = tag_route
        self.post_route = post_route
        self.search_route = search_route
        self.embed = embed

    def get_author(self, author_id):
        response = self.make_request(self.author_route, author_id)
        if response.status_code != 200:
            return None
        response = response.json()
        author = Author()
        author.__dict__.pop('_state')
        author.original_id = response.get('id')

        author.name = unescape(response.get('name'))
        author.link = response.get('link')
        author.slug = response.get('slug')
        author.cbDescription = response.get('cbDescription')
        author.position = response.get('position')
        if response.get('links'):
            author.twitter = response.get('links').get('twitter')
            author.facebook = response.get('links').get('facebook')
            author.homepage = response.get('links').get('homepage')
            author.crunchbase = response.get('links').get('crunchbase')
            author.linkedin = response.get('links').get('linkedin')

        author_instance, created = Author.objects.get_or_create(original_id=author.original_id,
                                                                defaults=author.__dict__)
        print(created)
        return author_instance

    def get_category(self, category_id):
        response = self.make_request(self.category_route, category_id)
        if response.status_code != 200:
            return None
        response = response.json()
        category = Category()
        category.__dict__.pop('_state')
        category.original_id = response.get('id')
        category.name = response.get('name')
        category.link = response.get('link')
        category.slug = response.get('slug')
        category.description = response.get('description')
        category_instance, created = Category.objects.get_or_create(original_id=category.original_id,
                                                                    defaults=category.__dict__)
        return category_instance

    def get_tag(self, tag_id):
        response = self.make_request(self.tag_route, tag_id)
        if response.status_code != 200:
            return None
        response = response.json()
        tag = Tag()
        tag.__dict__.pop('_state')
        tag.original_id = response.get('id')
        tag.name = response.get('name')
        tag.link = response.get('link')
        tag.slug = response.get('slug')
        tag.description = response.get('description')

        tag_instance, created = Tag.objects.get_or_create(original_id=tag.original_id, defaults=tag.__dict__)
        return tag_instance

    def get_post(self, post_id):
        response = self.make_request(self.post_route, post_id)
        if response.status_code != 200:
            return None
        response = response.json()
        post = Post()
        post.__dict__.pop('_state')
        post.original_id = response.get('id')
        post.link = response.get('link')
        post.slug = response.get('slug')
        post.original_creation_date = response.get('date')
        post.original_modification_date = response.get('modified')
        post.title = response.get('title').get('rendered')
        post.html_content = response.get('content').get('rendered')
        post_instance, created = Post.objects.get_or_create(original_id=post.original_id, defaults=post.__dict__)

        for author in response.get('authors'):
            author_instance = self.get_author(author)
            if author_instance is None:
                return None
            else:
                post_instance.authors.add(author_instance)

        for category in response.get('categories'):
            category_instance = self.get_category(category)
            if category_instance is None:
                return None
            else:
                post_instance.categories.add(category_instance)

        for tag in response.get('tags'):
            tag_instance = self.get_tag(tag)
            if tag_instance is None:
                return None
            else:
                post_instance.tags.add(tag_instance)

        post_instance.save()
        return post_instance, created

    def make_request(self, route, id=''):
        response = requests.get(
            f'{self.base_url}/{self.main_api_route}/{route}/{id}?&_embed={self.embed}&per_page=100')
        return response


    def get_posts(self):
        #last_post_id = Post.objects.latest('original_id').original_id if Post.objects.exists() else 0
        posts = self.make_request(self.post_route).json()
        print(len(posts))
        for post in posts:
            print(post['id'])
            # if post['id'] <= last_post_id:
            #     break
            self.get_post(post['id'])

    def search_post(self, query: str):
        url_param_formatted_string = quote(query)
        search_url = f'{self.base_url}/{self.main_api_route}/{self.search_route}?search={url_param_formatted_string}&type=post&_embed={self.embed}&per_page=100'
        response = requests.get(search_url)
        response.raise_for_status()
        keyword, created = Keyword.objects.get_or_create(keyword=query)
        max_pages = int(response.headers.get('x-wp-totalpages'))
        max_item = int(response.headers.get('x-wp-total'))
        if max_item > 0:
            for page in range(1, max_pages):
                response = requests.head(search_url + f"&page={page}&_envelope=false")
                for post in response.json():
                    post, created = self.get_post(post['id'])
                    SearchResult.objects.create(post=post, keyword=keyword)
        else:
            SearchResult.objects.create(keyword=keyword)
        return "Search Complete"
