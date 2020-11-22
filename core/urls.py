from django.urls import path

from . import views

urlpatterns = [
    path('match/<path:id>/', views.retriveMatch, name='match'),
    path('match/', views.listMatch, name='listmatch'),
    path('event/', views.Event, name='event'),
]
