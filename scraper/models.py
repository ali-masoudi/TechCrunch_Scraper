from django.db import models, transaction
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class BaseModel(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')
    modification_date = models.DateTimeField(auto_now=True, verbose_name='Modification Date')

    class Meta:
        abstract = True
        ordering = ('pk',)

    def __str__(self):
        raise NotImplementedError("You Must Implement This Method")


class BaseEntity(BaseModel):
    original_id = models.IntegerField(verbose_name='Original ID', null=True, blank=True)
    link = models.URLField(verbose_name='Link', null=True, blank=True)
    name = models.CharField(verbose_name='Name', null=True, blank=True, max_length=255)
    slug = models.SlugField(verbose_name='Slug', null=True, blank=True)
    count = models.IntegerField(verbose_name='Counts', default=0)
    original_creation_date = models.DateTimeField(verbose_name='Original Creation Date', null=True, blank=True)
    original_modification_date = models.DateTimeField(verbose_name='Original Modification Date', null=True, blank=True)

    class Meta:
        abstract = True
        ordering = ('pk',)

    def __str__(self):
        raise NotImplementedError("You Must Implement This Method")


class Author(BaseEntity):
    position = models.CharField(verbose_name='Position', null=True, blank=True, max_length=255)
    twitter = models.URLField(verbose_name='Twitter', null=True, blank=True)
    homepage = models.URLField(verbose_name='Homepage', null=True, blank=True, )
    facebook = models.URLField(verbose_name='Facebook', null=True, blank=True, )
    linkedin = models.URLField(verbose_name='linkedin', null=True, blank=True, )
    crunchbase = models.URLField(verbose_name='CrunchBase', null=True, blank=True)
    cbDescription = models.TextField(verbose_name="Description", null=True, blank=True )
    # Exclude These Fileds
    original_creation_date = None
    original_modification_date = None
    count = None

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return self.name


class Category(BaseEntity):
    description = models.TextField(verbose_name='Description', null=True, blank=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['name', ]

    def __str__(self):
        return f"{self.name} has {self.count} posts"


class Tag(BaseEntity):
    description = models.TextField(verbose_name='Description', null=True, blank=True)
    original_creation_date = None
    original_modification_date = None

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['-count']

    def __str__(self):
        return f"#{self.name} mentioned in {self.count} posts"


class Post(BaseEntity):
    title = models.CharField(verbose_name='Title', max_length=500)
    html_content = models.TextField(verbose_name='HTML Content', )
    authors = models.ManyToManyField(Author, related_name='posts',null=True,blank=True)
    categories = models.ManyToManyField(Category, related_name='posts')
    tags = models.ManyToManyField(Tag, related_name='posts')
    # primary_author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name='primary_posts')
    # primary_category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='primary_posts')

    # Exclude These Fileds
    name = None
    count = None

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-original_creation_date']

    def __str__(self):
        return f"{self.title}"


class Keyword(BaseModel):
    keyword = models.CharField(max_length=255, verbose_name="Keyword")
    modification_date = None

    def __str__(self):
        return self.keyword

    class Meta:
        verbose_name = "Keyword"
        verbose_name_plural = "Keywords"


class SearchResult(BaseModel):
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE, related_name='search_results')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='search_results')
    modification_date = None

    class Meta:
        verbose_name = 'Search Result'
        verbose_name_plural = 'Search Results'

    def __str__(self):
        return f"Keyword: {self.keyword.keyword} - Post: {self.post.title}"


@receiver(post_save, sender=Post)
@receiver(post_delete, sender=Post)
def update_category_post_count(sender, instance, **kwargs):
    with transaction.atomic():
        for category in instance.categories.all():
            category.count = category.posts.count()
            category.save()


@receiver(post_save, sender=Post)
@receiver(post_delete, sender=Post)
def update_tag_post_count(sender, instance, **kwargs):
    with transaction.atomic():
        for tag in instance.tags.all():
            tag.count = tag.posts.count()
            tag.save()
