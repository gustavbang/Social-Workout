from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:fitnessguy_id>/', views.detail, name='detail'),
    path('stats/<int:fitnessguy_id>', views.stats, name='stats'),

    path('login', auth_views.login, name='login'),
    path('logout', auth_views.logout, name='logout'),
    path('admin', admin.site.urls)
]