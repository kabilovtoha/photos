# -*- coding: utf-8 -*-

from django.db import connection

# from geo import models


def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
            dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()
    ]


def get_data(sql_str):
    cursor = connection.cursor()
    cursor.execute(sql_str)
    data = dictfetchall(cursor)

    return data