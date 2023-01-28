# Generated by Django 4.1.3 on 2022-12-13 15:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0007_remove_news_category_news_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelevantNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relevant_news', to='news.news')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relevant_news', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]