# Generated by Django 5.0.4 on 2024-05-06 18:15

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_myapp_delete_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myapp',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='会員番号'),
        ),
    ]
