# Generated by Django 4.2.10 on 2024-03-04 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0003_remove_post_count_alter_author_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='cbDescription',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
    ]
