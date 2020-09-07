from django.db import models

# Create your models here.
class GeneratedGraphs(models.Model):
    graph_name = models.CharField(max_length=200, default='default')
    graph_count = models.BigIntegerField('generated graph count',default=0)
    def __str__(self):
        return self.graph_name