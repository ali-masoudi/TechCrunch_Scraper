from django.db import models


class BaseModel(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')
    modification_date = models.DateTimeField(auto_now=True, verbose_name='Modification Date')
    base_id = models.IntegerField(verbose_name='base_id',null= False,blank=False)
    link = models.URLField(verbose_name='link',null= False,blank=False)
    class Meta:
        abstract = True
        ordering = ('pk',)

    def __str__(self):
        raise NotImplementedError("You Must Implement This Method")


class Keyword(BaseModel):
    keyword = models.CharField(max_length=255, verbose_name="Keyword")
    modification_date = None

    def __str__(self):
        return self.keyword

    class Meta:
        verbose_name = "Keyword"
        verbose_name_plural = "Keywords"


class Cetegory(BaseModel):
    category_id = models.CharField(max_length=255, verbose_name="Category ID")


class SearchResult(BaseModel):
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE, related_name='search_results')

    book = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='search_results')
    modification_date = None

    class Meta:
        verbose_name = 'Search Result'
        verbose_name_plural = 'Search Results'

    def __str__(self):
        return f"Keyword: {self.keyword.keyword} - Book: {self.post.title}"