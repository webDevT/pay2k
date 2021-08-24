# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from db.models import Rewards
from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse


def landing(request):
    import time
    # popular_games = Games.objects.filter(hide=False).order_by('-installs', '-id')[:13]
    # popular_games = list(popular_games)
    payouts = Rewards.objects.order_by('-timestamp')[:6]
    return render(request, 'site/index.html', {'rewards': payouts})

# def landing_load_games(request):
#     _popular_games = Games.objects.filter(hide=False, installs__lte=request.GET.get('installs'))\
#     .filter(~Q(id=request.GET.get('id'))).order_by('-installs', '-id')[:13]
#     _popular_games = list(_popular_games)
#     popular_games = []
#     for x in _popular_games:
#         popular_games.append({
#             'id': x.id,
#             'namespace': x.namespace,
#             'installs': x.installs,
#             'name': x.name,
#             'picture': x.picture.url,
#         })
#     response = {'popular_games': popular_games[:-1 if len(popular_games) == 13 else len(popular_games)]}
#     response['has_more_games'] = True if len(popular_games) == 13 else False
#     response = json.dumps(response)
#     return HttpResponse(response, content_type='application/json')

# def landing_load_rewards(request):
#     _rewards = Rewards.objects.filter(timestamp__lt=request.GET.get('timestamp')).order_by('-timestamp')[:6]
#     _rewards = list(_rewards)
#     rewards = []
#     for x in _rewards:
#         rewards.append({
#             'timestamp': x.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
#             'amount': x.amount,
#             'userpic': x.account.userpic.url if x.account.userpic else '/static/no_avatar.png',
#             'username': x.account.username,
#             'type': x.get_reward_type_display(),
#             'date': x.timestamp.strftime('%Y-%m-%d'),
#         })
#     response = {'rewards': rewards[:-1 if len(rewards) == 6 else len(rewards)]}
#     response['has_more_rewards'] = True if len(rewards) == 6 else False
#     response = json.dumps(response)
#     return HttpResponse(response, content_type='application/json')
