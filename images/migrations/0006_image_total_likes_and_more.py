# Generated by Django 4.1.11 on 2023-10-25 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0005_alter_image_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='total_likes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddIndex(
            model_name='image',
            index=models.Index(fields=['-total_likes'], name='images_imag_total_l_0bcd7e_idx'),
        ),
    ]
