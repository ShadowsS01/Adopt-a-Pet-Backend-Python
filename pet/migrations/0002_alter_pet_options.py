# Generated by Django 4.0.5 on 2022-06-10 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pet',
            options={'verbose_name_plural': 'Pets'},
        ),
    ]
