# Generated by Django 4.1.11 on 2023-10-19 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(default='/static/static/defaults/default.png', upload_to='images/%Y/%m/%d/'),
        ),
    ]