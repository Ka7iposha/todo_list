# Generated by Django 5.0.dev20230224080859 on 2023-04-04 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_category_todoitem_complete_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='todo_app.category', verbose_name='категория'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Article',
        ),
    ]
