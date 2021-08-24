import json
import time

from db.models import Account, Transactions, LevelCompletion, Raffle, RaffleTicket, RaffleParticipation, Rewards
from django.contrib import admin
from django.contrib.messages import error
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.safestring import mark_safe


class AccountAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_joined', 'invite_code', 'inviter', 'crystals', 'first_name', 'last_name', 'username']
    search_fields = ['user', 'username']
    raw_id_fields = ['inviter']
    actions = ['send_tc']

    def send_tc(self, request, queryset):
        if queryset.count() > 1:
            error(request, 'Transferring TC could operate only with 1 account at moment.')
            return redirect(request.META['HTTP_REFERER'])
        opts = self.model._meta
        user = queryset[0]
        return render(request, 'admin/account/tc-transfer.html', {'opts': opts, 'user': user})

    send_tc.short_description = "Send TC"


class TransactionsAdmin(admin.ModelAdmin):
    list_display = ['timestamp', 'account', 'crystals', 'reason', 'uid', 'level']
    raw_id_fields = ['account',]


class LevelCompletionAdmin(admin.ModelAdmin):
    list_display = ['account', 'uid', 'level']


class RaffleAdmin(admin.ModelAdmin):
    list_display = ['name', 'cost', 'end_tickets_sale', 'status', 'get_tickets_count', 'get_raffle_participants_link',
                    'prepare_winner_search_form']
    raw_id_fields = ['winner']
    actions = ['set_lottery_result_to_blockchain']

    def get_raffle_participants_link(self, object):
        return mark_safe('<a href="load-participants-csv/{0}/">Participants</a>'.format(object.id))

    get_raffle_participants_link.allow_tags = True

    def prepare_winner_search_form(self, object):
        return mark_safe('<a href="winner-search/?raffle={0}">Winner Search</a>'.format(object.id))

    def get_tickets_count(self, object):
        return object.participants.count()

    get_tickets_count.short_description = 'Tickets Count'

    def get_raffle_participants(self, request, raffle_id, *args, **kwargs):
        raffle = Raffle.objects.get(id=raffle_id)
        _csv = []
        for x in raffle.participations.iterator():
            for y in x.tickets.iterator():
                _csv.append(y.number)
        response = HttpResponse()
        response['Content-Type'] = "text/csv"
        response['Content-Disposition'] = "attachment;filename=participants.csv"
        response.write('\n'.join(_csv))
        return response

    def winner_search_form(self, request, *args, **kwargs):
        if request.GET.get('raffle'):
            request.session['raffle_form_id'] = request.GET.get('raffle')
            return HttpResponseRedirect(reverse('admin:get_raffle_winner_search_form'))
        if request.session.get('raffle_form_id'):
            context = {}
            if request.POST.get('ticket'):
                raffle_id = request.session.get('raffle_form_id')
                raffle = Raffle.objects.get(id=raffle_id)
                participant = raffle.participations.get(tickets__number=request.POST.get('ticket'))
                context['winner'] = participant.account
            return render(request, 'admin/raffle/winner_search_form.html', context)

    def get_urls(self, *args, **kwargs):
        base_urlpatterns = super(RaffleAdmin, self).get_urls(*args, **kwargs)
        from django.conf.urls import url

        urlpatterns = [
            url(r'^load-participants-csv/(\d+)/$',
                self.get_raffle_participants,
                name='get_raffle_participants'),
            url(r'^winner-search/$',
                self.winner_search_form,
                name='get_raffle_winner_search_form'),
        ]
        return urlpatterns + base_urlpatterns

    def set_lottery_result_to_blockchain(self, request, queryset):
        if queryset.count() > 1:
            error(request, 'Do separate raffles during this action.')
            return redirect(request.META['HTTP_REFERER'])
        obj = queryset[0]
        if not obj.winner:
            error(request, 'Winner is not fullfilled yet.')
            return redirect(request.META['HTTP_REFERER'])
        if not obj.status == 1:
            error(request, 'Raffle is not completed yet.')
            return redirect(request.META['HTTP_REFERER'])
        if not obj.winner_ticket:
            error(request, 'Won Ticket is not fullfilled yet.')
            return redirect(request.META['HTTP_REFERER'])

        structure_to_send = {
            'raffle_token': str(obj.id),
            'bgn_time': time.mktime(obj.created.timetuple()),
            'end_time': time.mktime(obj.end_tickets_sale.timetuple()),
            'raffle_time': time.mktime(obj.end_tickets_sale.timetuple()),
        }
        structure_to_send['tickets'] = [
            {
                'user_id': str(x.raffle_participation.account_id),
                'ticket_token': x.number,
            } for x in RaffleTicket.objects.filter(raffle_participation__raffle=obj).iterator()
        ]
        structure_to_send['winners'] = [
            {
                'user_id': obj.winner_id,
                'ticket_token': obj.winner_ticket,
                'win_tons': obj.prize,
                'message': '',
            }
        ]

        return render(request, 'admin/raffle/tokenize-result.html', {'data': json.dumps(
            {
                'action': 'tokenize_raffle',
                'data': structure_to_send,
            }
        )})

    set_lottery_result_to_blockchain.short_description = "Tokenize Raffle results"


class RaffleTicketInlineAdmin(admin.StackedInline):
    model = RaffleTicket


class RaffleParticipationAdmin(admin.ModelAdmin):
    list_display = ['account', 'raffle', 'winner', 'was_checked']
    raw_id_fields = ['account', 'raffle']
    inlines = [RaffleTicketInlineAdmin]

class RewardsAdmin(admin.ModelAdmin):
    list_display = ['timestamp', 'reward_type', 'account', 'amount', 'status']
    raw_id_fields = ['account']

admin.site.register(Account, AccountAdmin)
admin.site.register(Transactions, TransactionsAdmin)
admin.site.register(LevelCompletion, LevelCompletionAdmin)
admin.site.register(Raffle, RaffleAdmin)
admin.site.register(RaffleParticipation, RaffleParticipationAdmin)
admin.site.register(Rewards, RewardsAdmin)