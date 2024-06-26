# Generated by Django 5.0.2 on 2024-04-08 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presentation', '0004_zlide'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zlide',
            name='presentation',
        ),
        migrations.AddField(
            model_name='zlide',
            name='presentation_data',
            field=models.JSONField(default={'message': 'Presentation created successfully', 'presentation_data': [{'content': 'Welcome to Benson, your one-stop fashion destination. Our online store offers a wide range of trendy and affordable clothing, shoes, and accessories for men and women.', 'slide': 1, 'title': 'Introduction'}, {'content': "At Benson, we strive to bring you the latest fashion trends straight from the runway. Whether you're looking for casual everyday wear or a statement piece for a special occasion, we have you covered.", 'slide': 2, 'title': 'Shop the Latest Trends'}, {'content': 'With fast shipping, easy returns, and top-notch customer service, shopping at Benson is a breeze. Join our community of fashion-forward individuals and elevate your style with our curated collection of must-have pieces.', 'slide': 3, 'title': 'Why Choose Benson?'}]}),
            preserve_default=False,
        ),
    ]
