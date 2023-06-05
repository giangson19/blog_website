from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    # path('', views.PostList.as_view(), name = 'home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name = 'post_detail'),
    # path('about/', views.About.as_view(), name = 'about'),    
]
