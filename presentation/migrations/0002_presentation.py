# Generated by Django 5.0.2 on 2024-04-08 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presentation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Presentation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('slide', models.CharField(max_length=256)),
                ('content', models.TextField()),
            ],
        ),
    ]
