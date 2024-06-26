# Generated by Django 5.0.2 on 2024-04-20 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='company',
            field=models.CharField(blank=True, default='No company specified', max_length=255, null=True, verbose_name='company name'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(error_messages={'unique': 'A user with this email already exists.'}, max_length=255, unique=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='job_title',
            field=models.CharField(blank=True, default='No Job specified', max_length=255, null=True, verbose_name='job title'),
        ),
    ]
