# Generated by Django 3.2.8 on 2021-10-07 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='image_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='image_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='location_name',
            new_name='name',
        ),
        migrations.AddField(
            model_name='image',
            name='category',
            field=models.ManyToManyField(to='gallery.Category'),
        ),
        migrations.AddField(
            model_name='image',
            name='location',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='gallery.location'),
        ),
    ]
