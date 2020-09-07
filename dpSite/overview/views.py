from django.shortcuts import render
from django.http import HttpResponse
from graph.models import GeneratedGraphs

# Create your views here.
def index(request):
    graph = GeneratedGraphs.objects.get(pk=1)
    GraphCount = 'We generated %d graphs!' % graph.graph_count
    return HttpResponse("This will be the simple landing page. %s" % GraphCount)