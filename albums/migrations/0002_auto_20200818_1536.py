# Generated by Django 3.1 on 2020-08-18 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='content',
            field=models.TextField(),
        ),
    ]