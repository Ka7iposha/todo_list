# Generated by Django 5.0.dev20230224080859 on 2023-04-04 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0003_todoitem_category_delete_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='category',
            field=models.ForeignKey(default='general', on_delete=django.db.models.deletion.CASCADE, to='todo_app.category', verbose_name='категория'),
        ),
    ]
