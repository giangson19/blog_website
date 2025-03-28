from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('', views.AllPostsList.as_view(), name = 'all_posts'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('<slug:slug>/', views.PostDetail.as_view(), name = 'post_detail'),
]
