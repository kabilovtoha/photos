# -*- coding: utf-8 -*-
from rest_framework import serializers
from . import models
from django.contrib.auth.models import User




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.City
        fields = [
            'id', 'name',
        ]

class PhotoSerializer(serializers.ModelSerializer):
    # url_detail = serializers.URLField(source='get_detail_url', read_only=True)
    image_thumbnail = serializers.URLField(source='get_image_thumbnail')
    class Meta:
        model = models.Photo
        fields = [
            'id', 'author', 'city', 'image', 'image_thumbnail', 'desc', 'is_published', #'url_detail'
        ]
class PhotoDetailSerializer(PhotoSerializer):
    city = CitySerializer()
    username = serializers.CharField(source='get_username')
    class Meta:
        model = models.Photo
        fields = [
            'id', 'author', 'city', 'image', 'image_thumbnail', 'desc', 'is_published', 'created', 'username'
        ]
