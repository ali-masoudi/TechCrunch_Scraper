# Generated by Django 4.2.10 on 2024-03-04 15:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('scraper', '0002_remove_author_twitter_id_author_twitter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='count',
        ),
        migrations.AlterField(
            model_name='author',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='Link'),
        ),
        migrations.AlterField(
            model_name='author',
            name='original_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='Original ID'),
        ),
        migrations.AlterField(
            model_name='author',
            name='slug',
            field=models.SlugField(blank=True, null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='category',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='Link'),
        ),
        migrations.AlterField(
            model_name='category',
            name='original_creation_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Original Creation Date'),
        ),
        migrations.AlterField(
            model_name='category',
            name='original_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='Original ID'),
        ),
        migrations.AlterField(
            model_name='category',
            name='original_modification_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Original Modification Date'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='post',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='Link'),
        ),
        migrations.AlterField(
            model_name='post',
            name='original_creation_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Original Creation Date'),
        ),
        migrations.AlterField(
            model_name='post',
            name='original_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='Original ID'),
        ),
        migrations.AlterField(
            model_name='post',
            name='original_modification_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Original Modification Date'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='Link'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='original_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='Original ID'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(blank=True, null=True, verbose_name='Slug'),
        ),
    ]
