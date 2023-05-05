from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns=[
    path('',views.home, name='home'),
    path('<str:room>/',views.room,name='room'),
    path('checkview',views.checkview, name='checkview'),
    path('send',views.send, name='send'),
    path('getMessages/<str:room>/',views.getMessages,name='getMessages'),
    path('go_home/', views.go_home, name='go_home'),
]
