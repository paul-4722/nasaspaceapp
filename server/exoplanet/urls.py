from django.contrib import admin
from django.urls import path

import exoplanet.views as views

urlpatterns = [
    path("main/", views.LandingView.as_view()), 
    path("star/list/", views.StarListView.as_view()),
    path("star/<int:pk>/", views.StarDetailedView.as_view()), 
    path("star/<str:name>/", views.StarDetailedViewByAuthor.as_view()), 
    path("star/<int:pk>/create/", views.PlanetCreateView.as_view()), 
    path("planet/list/<str:option>/", views.PlanetListView.as_view()), 
    path("planet/<int:pk>/", views.PlanetDetailedView.as_view()),
    path("quests/<str:name>/", views.QuestListView.as_view()), 
    path("quests/<str:name>/<int:number>/", views.QuestCompleteView.as_view()), 
    path("points/<str:name>/", views.PointsView.as_view()), 
]

'''
main/ : landing page
star/list : star의 list
star/<int:pk>/ : star의 각 정보, id로 접근
star/<str:name>/ : star의 각 정보, 해당 별을 소유한 유저 이름으로 접근(검색용)
star/<int:pk>/create/ : star의 자식 planet 제작
planet/list/<str:option>/ : 전체 planet의 list. 
                            option  - normal(모든 행성), 
                                    - original(현실에 존재하는 행성), 
                                    - user(유저가 만든 행성)
planet/<int:pk>/ : planet의 각 정보, id로 접근
quests/<str:name>/ : name 이름 가진 유저의 quest 정보
quests/<str:name>/<int:number>/ : POST 요청을 보냈을 때, name 이름 가진 유저의 number번 quest를 complete 상태로 변환. 
points/<str:name>/ : 유저의 포인트 정보를 보여줌. POST 요청을 통해 포인트 변화 가능. 

* quest 생성은 유저가 생성될 때 일어남. 지금은 1개의 quest만이 만들어지도록 설정된 상태. 
'''
