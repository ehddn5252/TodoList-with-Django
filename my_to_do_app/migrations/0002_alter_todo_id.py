# Generated by Django 4.0.3 on 2022-04-11 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_to_do_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
