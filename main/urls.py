from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("signup", views.signup, name='signup'),
    path("login", views.login, name='login'),
    path("logout", views.logout, name='logout'),
    path("upload", views.upload, name='upload'),
    path('profile', views.self_profile, name='self_profile0'),
    path('profile/',views.self_profile, name='self_profile1'),
    path('profile/<slug:username>/', views.profile, name='profile'),
    path('image/<int:id>/', views.full_page_image, name='full_page_image' ),
    path('edit-profile', views.edit_profile, name='edit-profile'),
    path('search/<slug:key>', views.search, name='search')
]