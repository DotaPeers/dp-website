# Generated by Django 3.1 on 2020-09-07 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0002_auto_20200907_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='generatedgraphs',
            name='graph_name',
            field=models.CharField(default='default', max_length=200),
        ),
    ]
