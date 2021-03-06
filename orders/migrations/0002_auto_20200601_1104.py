# Generated by Django 3.0.6 on 2020-06-01 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubTopping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=2, default=0.5, max_digits=3)),
            ],
        ),
        migrations.AlterField(
            model_name='other',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.CreateModel(
            name='Sub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64)),
                ('size', models.CharField(blank=True, max_length=64)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('toppings', models.ManyToManyField(blank=True, to='orders.SubTopping')),
            ],
        ),
    ]
