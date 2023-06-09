# Generated by Django 4.2.1 on 2023-06-21 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_image_created_alter_image_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='image',
            name='total_likes',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AddIndex(
            model_name='image',
            index=models.Index(fields=['-created'], name='images_imag_created_d57897_idx'),
        ),
        migrations.AddIndex(
            model_name='image',
            index=models.Index(fields=['-total_likes'], name='images_imag_total_l_0bcd7e_idx'),
        ),
    ]
