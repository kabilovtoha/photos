# -*- coding: utf-8 -*-

from elasticsearch_dsl import (
    Document,
    Date,
    Keyword,
    Text,
    Boolean,
    Integer
)

class PhotoIndex(Document):

    pk = Integer()
    city_id = Integer()
    created = Date()
    is_published = Boolean()

    class Meta:
        index = 'Photo'


# PhotoIndex.init()
