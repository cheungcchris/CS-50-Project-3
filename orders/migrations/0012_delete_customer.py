# Generated by Django 3.0.6 on 2020-06-05 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_auto_20200603_1225'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer',
        ),
    ]