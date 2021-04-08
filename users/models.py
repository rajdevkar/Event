from django.db import models
from django.contrib.auth.models import User

class Tournament(models.Model):
    LEVEL = (
        ('state_level', 'State Level'),
        ('district_level', 'District Level'),
    )

    TOURNAMENTS = (
        ('football', 'Football'),
        ('cricket', 'Cricket'),
        ('volley_ball', 'Volley Ball'),
        ('hockey', 'Hockey'),
        ('badminton', 'Badminton'),
        ('basket_ball', 'Basket Ball'),
    )

    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    level = models.CharField(max_length=20, choices=LEVEL)
    tournament = models.CharField(max_length=20, choices=TOURNAMENTS)
    gender = models.CharField(max_length=20, choices=GENDER)
    date = models.DateField(blank=True, null=True)
    added_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='added_by')
    venue = models.CharField(max_length=60)

    def __unicode__(self):
        return self.tournament

class Winners(models.Model):
    winners_for = models.ForeignKey(
        Tournament, on_delete=models.CASCADE, related_name='winners_for')
    gold = models.CharField(max_length=100)
    silver = models.CharField(max_length=100)
    bronze = models.CharField(max_length=100)

    def __unicode__(self):
        return self.winners_for

class Participated(models.Model):
    participate_for = models.ForeignKey(
        Tournament, on_delete=models.CASCADE, related_name='participate_for')
    team_name = models.CharField(max_length=100)
    player_1 = models.CharField(max_length=100)
    player_2 = models.CharField(max_length=100)
    player_3 = models.CharField(max_length=100)
    player_4 = models.CharField(max_length=100)
    player_5 = models.CharField(max_length=100)
    player_6 = models.CharField(max_length=100)
    player_7 = models.CharField(max_length=100)
    player_8 = models.CharField(max_length=100)
    player_9 = models.CharField(max_length=100)
    player_10 = models.CharField(max_length=100)
    player_11 = models.CharField(max_length=100)

    def __unicode__(self):
        return self.participate_for

class StaffEntry(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __unicode__(self):
        return self.winners_for