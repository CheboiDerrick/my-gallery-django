# Generated by Django 3.2.8 on 2021-10-08 12:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20211007_1646'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['post_time']},
        ),
        migrations.AddField(
            model_name='image',
            name='post_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
