# Generated by Django 3.1.2 on 2020-10-13 02:19

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20, verbose_name='タイトル')),
                ('text', models.CharField(max_length=200, verbose_name='本文')),
                ('price', models.IntegerField(null=True, verbose_name='価格')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'post',
            },
        ),
    ]