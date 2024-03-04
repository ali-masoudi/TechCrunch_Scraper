# Generated by Django 4.2.10 on 2024-03-04 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('modification_date', models.DateTimeField(auto_now=True, verbose_name='Modification Date')),
                ('original_id', models.IntegerField(unique=True, verbose_name='Original ID')),
                ('link', models.URLField(verbose_name='Link')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('twitter_id', models.CharField(max_length=255, verbose_name='Twitter ID')),
                ('position', models.CharField(blank=True, max_length=255, null=True, verbose_name='Position')),
                ('homepage', models.URLField(blank=True, null=True, verbose_name='Homepage')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Facebook')),
                ('linkedin', models.URLField(blank=True, null=True, verbose_name='linkedin')),
                ('crunchbase', models.URLField(blank=True, null=True, verbose_name='CrunchBase')),
                ('cbDescription', models.TextField(verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('modification_date', models.DateTimeField(auto_now=True, verbose_name='Modification Date')),
                ('original_id', models.IntegerField(unique=True, verbose_name='Original ID')),
                ('link', models.URLField(verbose_name='Link')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('count', models.IntegerField(default=0, verbose_name='Counts')),
                ('original_creation_date', models.DateTimeField(verbose_name='Original Creation Date')),
                ('original_modification_date', models.DateTimeField(verbose_name='Original Modification Date')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('keyword', models.CharField(max_length=255, verbose_name='Keyword')),
            ],
            options={
                'verbose_name': 'Keyword',
                'verbose_name_plural': 'Keywords',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('modification_date', models.DateTimeField(auto_now=True, verbose_name='Modification Date')),
                ('original_id', models.IntegerField(unique=True, verbose_name='Original ID')),
                ('link', models.URLField(verbose_name='Link')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('count', models.IntegerField(default=0, verbose_name='Counts')),
                ('original_creation_date', models.DateTimeField(verbose_name='Original Creation Date')),
                ('original_modification_date', models.DateTimeField(verbose_name='Original Modification Date')),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('html_content', models.TextField(verbose_name='HTML Content')),
                ('authors', models.ManyToManyField(related_name='posts', to='scraper.author')),
                ('categories', models.ManyToManyField(related_name='posts', to='scraper.category')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'ordering': ['-original_creation_date'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('modification_date', models.DateTimeField(auto_now=True, verbose_name='Modification Date')),
                ('original_id', models.IntegerField(unique=True, verbose_name='Original ID')),
                ('link', models.URLField(verbose_name='Link')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('count', models.IntegerField(default=0, verbose_name='Counts')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
                'ordering': ['-count'],
            },
        ),
        migrations.CreateModel(
            name='SearchResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('keyword', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='search_results', to='scraper.keyword')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='search_results', to='scraper.post')),
            ],
            options={
                'verbose_name': 'Search Result',
                'verbose_name_plural': 'Search Results',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(related_name='posts', to='scraper.tag'),
        ),
    ]