# Generated by Django 2.2.7 on 2019-11-21 07:06

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0008_auto_20191121_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='image_thumb',
            field=imagekit.models.fields.ProcessedImageField(upload_to=''),
        ),
    ]
