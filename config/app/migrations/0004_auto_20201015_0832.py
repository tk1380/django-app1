# Generated by Django 3.1.2 on 2020-10-14 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20201014_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='本文'),
        ),
    ]