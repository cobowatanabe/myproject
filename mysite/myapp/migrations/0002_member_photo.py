# Generated by Django 5.0.4 on 2024-05-05 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='member_photos/', verbose_name='顔写真'),
        ),
    ]