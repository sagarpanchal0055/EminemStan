# Generated by Django 3.1 on 2020-08-18 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lyrics', '0004_delete_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='lyrics',
            name='album_id',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]