# Generated by Django 3.2.6 on 2021-12-27 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tg', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='birthplace',
            field=models.TextField(blank=True, null=True, verbose_name='Место рождения'),
        ),
    ]
