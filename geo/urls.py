# -*- coding: utf-8 -*-

from django.conf import settings
from rest_framework import routers
from django.urls import path, include, re_path

from . import views
from . import rest_views

app_name = 'geo'

router = routers.DefaultRouter()

router.register('photo', rest_views.PhotoViewSet, basename='photo')


urlpatterns = [
    path('', views.IndexView.as_view()),
    path('photo/', views.PhotoView.as_view()),
    path('photo/city/<int:city_id>/', views.PhotoView.as_view()),
    path('photo/add/', views.PhotoAddView.as_view()),
    path('photos-filterparams/', views.get_photos_filterparams),

    path('api/v1/', include(router.urls)),
]
