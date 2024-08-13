# Generated by Django 3.2 on 2021-04-25 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newspaper', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('BUSINESS', 'Business'), ('CARS', 'Cars'), ('ENTERTAINMENT', 'Entertainment'), ('FAMILY', 'Family'), ('HEALTH', 'Health'), ('POLITICS', 'Politics'), ('RELIGION', 'Religion'), ('SCIENCE', 'Science'), ('SPORTS', 'Sports'), ('TECHNOLOGY', 'Technology'), ('TRAVEL', 'Travel'), ('VIDEO', 'Video'), ('WORLD', 'World')], default='POLITICS', max_length=100)),
                ('news_text', models.CharField(max_length=5000)),
            ],
        ),
    ]
