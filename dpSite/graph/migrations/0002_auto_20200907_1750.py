# Generated by Django 3.1 on 2020-09-07 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generatedgraphs',
            name='graphs_count',
        ),
        migrations.AddField(
            model_name='generatedgraphs',
            name='graph_count',
            field=models.BigIntegerField(default=0, verbose_name='generated graph count'),
        ),
    ]
