# Generated by Django 4.0.3 on 2022-04-11 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0004_alter_todo_todo_due_alter_todo_todo_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='Todo_detail',
            field=models.TextField(blank=True),
        ),
    ]