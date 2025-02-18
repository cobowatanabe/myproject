# Generated by Django 5.0.4 on 2024-05-05 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_member_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='op1_description',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='オプション1内容'),
        ),
        migrations.AddField(
            model_name='member',
            name='op1_fee',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='オプション1料金'),
        ),
        migrations.AddField(
            model_name='member',
            name='op2_description',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='オプション2内容'),
        ),
        migrations.AddField(
            model_name='member',
            name='op2_fee',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='オプション2料金'),
        ),
        migrations.AddField(
            model_name='member',
            name='op3_description',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='オプション3内容'),
        ),
        migrations.AddField(
            model_name='member',
            name='op3_fee',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='オプション3料金'),
        ),
    ]
