# Generated by Django 4.0.4 on 2022-07-10 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click the link to read full post', max_length=255),
        ),
    ]