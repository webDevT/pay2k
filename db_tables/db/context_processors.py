import pymysql
from django.urls import resolve
from django.db import connections


def landing_counters(request):
    return {}