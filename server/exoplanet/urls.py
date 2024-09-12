from django.contrib import admin
from django.urls import path

import exoplanet.views as views

urlpatterns = [
    path("main/", views.StarListView.as_view()),
    path("star/<int:pk>/", views.StarDetailedView.as_view()), 
    path("star/<int:pk>/create/", views.PlanetCreateView.as_view()), 
    path("planet/list/", views.PlanetListView.as_view()), 
    path("planet/list/<int:pk>/", views.PlanetDetailedView.as_view()), 
    
]

