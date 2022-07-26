# Generated by Django 4.0.6 on 2022-07-26 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoTask', '0002_alter_todo_creation_date_alter_todo_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='creation_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='description',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='due_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date due'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='tags',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
