# Generated by Django 4.0.6 on 2022-08-03 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoTask', '0003_alter_todo_creation_date_alter_todo_description_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['creation_date']},
        ),
    ]
