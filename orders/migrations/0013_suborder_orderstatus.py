# Generated by Django 3.0.6 on 2020-06-05 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_delete_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='suborder',
            name='orderstatus',
            field=models.CharField(default='pending', max_length=64),
        ),
    ]
