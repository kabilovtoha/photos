
# -*- coding: utf-8 -*-
from rest_framework import viewsets, mixins
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
# from django.contrib.auth.decorators import login_required
# from rest_framework import generics
# from django.utils.decorators import method_decorator

import django_filters


from . import models
from . import serializers
from . import paginations
from . import filters


class PhotoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Photo.objects.all()
    serializer_class = serializers.PhotoDetailSerializer
    pagination_class = paginations.PhotoPagination
    lookup_field = 'pk'
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = filters.PhotoFilterSet

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)
        return queryset
