# Generated by Django 5.1 on 2024-08-15 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='date_updated',
            field=models.DateTimeField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
