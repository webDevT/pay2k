import pymysql
from django.urls import resolve
from django.db import connections
from django.conf import settings


def landing_counters(request):
    static_prefix = '' if settings.DEBUG__ else 'https://d1dnz8glxzkhnm.cloudfront.net'
    env = {'static_prefix': static_prefix}
    return env