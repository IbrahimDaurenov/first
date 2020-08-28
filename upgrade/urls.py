from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'komp_index'),
    path('upgrade/',views.upgrade, name = 'komp_upgrade'),
    path('site/', views.site, name = 'site'),
    path('types/',views.types, name = 'types'),
    path('game/', views.game, name = 'game'),
    path('games/', views.games, name = 'games'),
    ]
