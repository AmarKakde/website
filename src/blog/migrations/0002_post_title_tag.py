# Generated by Django 5.0.7 on 2024-08-03 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Awesome Blog', max_length=255),
        ),
    ]
