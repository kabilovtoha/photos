# -*- coding: utf-8 -*-
from django_filters import rest_framework as filters

from . import models

class PhotoFilterSet(filters.FilterSet):
    photos_count = filters.CharFilter(method='photos_count_filter')
    class Meta:
        model = models.Photo
        fields = {
            'id': ['exact', 'in'],
            'city': ['exact', 'in'],
        }


    def photos_count_filter(self, queryset, name, value):
        if value:
            queryset = queryset.filter(rubrika__slug=value)

        return queryset