# Generated by Django 5.1 on 2024-08-15 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('subheading_1', models.CharField(blank=True, max_length=255, null=True)),
                ('subheading_2', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
