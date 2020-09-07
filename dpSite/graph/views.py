from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def plotter(request, player_id):
	return HttpResponse('This will show the graph of the player with the player id %s' % player_id)