# Generated by Django 2.1.1 on 2018-09-29 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0002_auto_20180929_1729'),
        ('products', '0012_auto_20180928_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(blank=True, to='tags.Tag'),
        ),
    ]
