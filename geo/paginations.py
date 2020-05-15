# -*- coding: utf-8 -*-
from collections import OrderedDict

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class BasePagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response(
            OrderedDict(
                [
                    ('current_page', self.page.number),
                    ('next', self.get_next_page_number()),
                    ('previous', self.get_previous_page_number()),
                    ('links', {
                        'next': self.get_next_link(),
                        'previous': self.get_previous_link()
                    }),
                    ('count', self.page.paginator.count),
                    ('page_size', self.page_size),
                    ('pages', self.page.paginator.num_pages),
                    ('results', data),
                ]
            )
        )

    def get_next_page_number(self):
        if not self.page.has_next():
            return None
        return self.page.next_page_number()

    def get_previous_page_number(self):
        if not self.page.has_previous():
            return None
        return self.page.previous_page_number()

class PhotoPagination(BasePagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 5

