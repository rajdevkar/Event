from django.db import models

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