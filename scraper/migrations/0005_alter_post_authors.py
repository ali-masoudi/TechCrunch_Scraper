# Generated by Django 4.2.10 on 2024-03-04 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0004_alter_author_cbdescription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='authors',
            field=models.ManyToManyField(blank=True, null=True, related_name='posts', to='scraper.author'),
        ),
    ]
