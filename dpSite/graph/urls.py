from django.urls import path

from . import views

app_name = 'graph'
urlpatterns = [
    path('<int:player_id>/', views.plotter, name='plotter'),
]