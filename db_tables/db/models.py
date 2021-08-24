import uuid
from django.db import models


class Account(models.Model):
    user = models.CharField(max_length=64, db_index=True, blank=True, null=True, unique=True)
    email = models.CharField(max_length=128, db_index=True, blank=True, null=True, unique=True)
    crystals = models.IntegerField(default=0, db_index=True, verbose_name='Crystals(delta)')
    first_name = models.CharField(max_length=64, blank=True, null=True)
    last_name = models.CharField(max_length=64, blank=True, null=True)
    username = models.CharField(max_length=64, blank=True, null=True, db_index=True)
    userpic = models.CharField(max_length=128, blank=True)
    date_joined = models.DateTimeField()
    date_last_interaction = models.DateTimeField(db_index=True)
    locale = models.CharField(max_length=8, blank=True)
    country = models.CharField(max_length=2, db_index=True, blank=True, null=True)
    invite_code = models.CharField(max_length=32, null=True, db_index=True)
    inviter = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    handled_profile = models.BooleanField()
    wallet = models.CharField(max_length=96, blank=True, null=True, unique=True)
    ft_wallet = models.CharField(max_length=96, blank=True, null=True, unique=True)
    is_surf_linked = models.BooleanField(default=False)

    gender = models.PositiveSmallIntegerField(
        choices=(
            (2, 'male'),
            (1, 'female'),
            (3, 'other'),
        ), blank=True, null=True
    )
    birthday = models.DateField(blank=True, null=True)
    marital_status = models.PositiveSmallIntegerField(
        choices=(
            (0, 'single'),
            (1, 'married'),
            (2, 'divorced'),
            (3, 'living with partner'),
            (4, 'separated'),
            (5, 'widow'),
            (6, 'prefer not to say'),
        ), blank=True, null=True
    )
    kids = models.PositiveSmallIntegerField(
        choices=(
            (0, '0'),
            (1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6+'),
            (7, 'prefer not to say'),
        ), blank=True, null=True
    )
    education = models.PositiveSmallIntegerField(
        choices=(
            (0, 'elementary school'),
            (1, 'middle school'),
            (2, 'high school'),
            (3, 'vocational technical college'),
            (4, 'university'),
            (5, 'post graduate'),
        ), blank=True, null=True
    )
    employment = models.PositiveSmallIntegerField(
        choices=(
            (0, 'EMPLOYED_FOR_WAGES'),
            (1, 'self emplyed'),
            (2, 'unemployed (looking for)'),
            (3, 'unemployed (not looking for)'),
            (4, 'homemaker'),
            (5, 'student'),
            (6, 'military'),
            (7, 'retired'),
            (8, 'unable to work'),
            (9, 'other'),
        ), blank=True, null=True
    )
    career = models.PositiveSmallIntegerField(
        choices=(
            (0, 'agriculture forestry fishing or hunting'),
            (1, 'arts entertainment or recreation'),
            (2, 'broadcasting'),
            (3, 'construction'),
            (4, 'education'),
            (5, 'finance and insurance'),
            (6, 'government and public administration'),
            (7, 'health care and social assistance'),
            (8, 'homemaker'),
            (9, 'hotel and food services'),
            (10, 'information other'),
            (11, 'information services and data'),
            (12, 'legal services'),
            (13, 'manufacturing computer and electronics'),
            (14, 'manufacturing other'),
            (15, 'military'),
            (16, 'mining'),
            (17, 'processing'),
            (18, 'publishing'),
            (19, 'real estate rental or leasing'),
            (20, 'religious'),
            (21, 'retail'),
            (22, 'retired'),
            (23, 'scientific or technical services'),
            (24, 'software'),
            (25, 'student'),
            (26, 'telecommunications'),
            (27, 'transportation and warehousing'),
            (28, 'unemployed'),
            (29, 'energy utilities oil and gas'),
            (30, 'wholesale'),
            (31, 'other'),
            (32, 'advertising'),
            (33, 'automotive'),
            (34, 'consulting'),
            (35, 'fashion apparel'),
            (36, 'human resources'),
            (37, 'market research'),
            (38, 'marketing sales'),
            (39, 'shipping distribution'),
            (40, 'personal services'),
            (41, 'security'),
        ), blank=True, null=True
    )
    race = models.PositiveSmallIntegerField(
        choices=(
            (0, 'arab'),
            (1, 'asian'),
            (2, 'black'),
            (3, 'white'),
            (4, 'hispanic'),
            (5, 'latino'),
            (6, 'multiracial'),
            (7, 'other'),
            (8, 'prefer not to say'),
        ), blank=True, null=True
    )
    income = models.PositiveSmallIntegerField(
        choices=(
            (0, 'lower 1'),
            (1, 'lower 2'),
            (2, 'middle 1'),
            (3, 'middle 2'),
            (4, 'high 1'),
            (5, 'high 2'),
            (6, 'high 3'),
            (7, 'prefer not to say'),
        ), blank=True, null=True
    )

    def __unicode__(self):
        return self.user or self.username or '-'

class Transactions(models.Model):
    timestamp = models.DateTimeField(db_index=True)
    day = models.DateField(db_index=True, blank=True, null=True)
    month = models.DateField(db_index=True, blank=True, null=True)
    crystals = models.IntegerField()
    reason = models.PositiveSmallIntegerField(
        choices=(
            (0, 'Redeem Rewards'),
            (1, 'Level completed'),
            (2, 'User registered'),
            (3, 'Survey'),
            (4, 'Offer Fyber'),
            (5, 'Offer Pollfish'),
            (6, 'Offer TapJoy'),
            (7, 'Rewarded Video'),
            (8, 'Offer IronSrc'),
            (9, 'Game First Install'),
            (10, 'Raffle ticket'),
            (11, 'Least from delta wirhdraw'),
        ), db_index=True
    )
    uid = models.CharField(max_length=128, null=True, db_index=True, blank=True)
    level = models.PositiveIntegerField(null=True, db_index=True, blank=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    raffle = models.ForeignKey('Raffle', blank=True, null=True, on_delete=models.CASCADE)
    source = models.CharField(max_length=128, null=True, blank=True)


class LevelCompletion(models.Model):
    level = models.PositiveIntegerField(null=True, db_index=True)
    uid = models.CharField(max_length=128, null=True, db_index=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['uid', 'account']

class Raffle(models.Model):
    name = models.CharField(max_length=64)
    cost = models.PositiveIntegerField()
    short_description = models.TextField()
    description = models.TextField()
    created = models.DateTimeField()
    end_tickets_sale = models.DateTimeField()
    status = models.PositiveSmallIntegerField(
        choices=(
            (0, 'Active'),
            (1, 'Finished')
        ), db_index=True
    )
    participants = models.ManyToManyField(Account, through='RaffleParticipation', related_name='raffles')
    winner = models.ForeignKey('Account', default=None, blank=True, null=True, on_delete=models.SET_NULL)
    winner_ticket = models.CharField(max_length=10, db_index=True, null=True, blank=True)
    prize = models.FloatField()

class RaffleParticipation(models.Model):
    account = models.ForeignKey('Account', on_delete=models.CASCADE)
    raffle = models.ForeignKey('Raffle', related_name='participations', on_delete=models.CASCADE)
    winner = models.BooleanField(default=False)
    was_checked = models.BooleanField(default=False)

    class Meta:
        unique_together = ['account', 'raffle']

class RaffleTicket(models.Model):
    raffle_participation = models.ForeignKey(RaffleParticipation, related_name='tickets', on_delete=models.CASCADE)
    bought_time = models.DateTimeField(db_index=True)
    number = models.CharField(max_length=10, db_index=True, unique=True)

class PollfishUniqueTransaction(models.Model):
    uid = models.CharField(max_length=48, unique=True)

class Rewards(models.Model):
    reward_type = models.PositiveIntegerField(
        choices=(
            (1, 'Leaderboard position'),
            (2, 'Raffle'),
        ), db_index=True
    )
    amount = models.FloatField()
    rate = models.FloatField()
    timestamp = models.DateTimeField(db_index=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    status = models.PositiveSmallIntegerField(
        choices=(
            (1, 'Info needed'),
            (2, 'Processing'),
            (3, 'Paid'),
        ), db_index=True
    )
    user_details = models.TextField(null=True, blank=True)