# Generated by Django 4.0.5 on 2022-06-21 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plugin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tache',
            name='date',
            field=models.DateField(),
        ),
    ]