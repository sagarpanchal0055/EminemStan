# Generated by Django 3.1 on 2020-08-18 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0002_auto_20200818_1536'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kamikaze',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.CharField(max_length=100)),
                ('content', models.TextField()),
            ],
        ),
    ]