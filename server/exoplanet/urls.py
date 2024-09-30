from django.contrib import admin
from django.urls import path

import exoplanet.views as views

urlpatterns = [
    path("main/", views.LandingView.as_view()), 
    path("star/list/", views.StarListView.as_view()),
    path("star/<int:pk>/", views.StarDetailedView.as_view()), 
    path("star/<int:pk>/create/", views.PlanetCreateView.as_view()), 
    path("planet/list/", views.PlanetListView.as_view()), 
    path("planet/<int:pk>/", views.PlanetDetailedView.as_view()), 
    
]

'''
main/ : landing page
star/list : star의 list
star/<int:pk>/ : star의 각 정보, id로 접근
star/<int:pk>/create/ : star의 자식 planet 제작
planet/list/ : 전체 planet의 list
planet/<int:pk>/ : planet의 각 정보, id로 접근
'''
