from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.utils.html import escape
from django.contrib import messages 
from django.forms.models import model_to_dict
from datetime import datetime

from .forms import CustomUserCreationForm, TournamentForm, WinnerForm
from .models import Tournament, Winners

def dashboard(request):
    return render(request, "users/dashboard.html")

def login_excluded(redirect_to):
    """ This decorator kicks authenticated users out of a view """ 
    def _method_wrapper(view_method):
        def _arguments_wrapper(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect(redirect_to) 
            return view_method(request, *args, **kwargs)
        return _arguments_wrapper
    return _method_wrapper

@login_excluded('dashboard')
def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))


## Tournament JSON
class TournamentJson(BaseDatatableView):
    tournament = Tournament
    columns = ['id', 'level', 'tournament', 'gender', 'date', 'venue']

    def filter_queryset(self, qs):
        search = self.request.GET.get(u'search[value]', None)
        if search:
            qs = qs.filter(tournament__startswith=search)
        return qs

    def get_initial_queryset(self):
        return Tournament.objects.all()

    def render_column(self, row, column):
        return super(TournamentJson, self).render_column(row, column)

## Winner JSON
class WinnerJson(BaseDatatableView):
    winners = Winners
    columns = ['id', 'winners_for_id', 'gold', 'silver', 'bronze']

    def filter_queryset(self, qs):
        search = self.request.GET.get(u'search[value]', None)
        if search:
            qs = qs.filter(winners_for__startswith=search).filter(gold=search).filter(silver=search).filter(bronze=search)
        return qs

    def get_initial_queryset(self):
        return Winners.objects.all()

    def render_column(self, row, column):
        return super(WinnerJson, self).render_column(row, column)

def tournaments(request):
    return render(request, "tournament/main.html")

def winners(request):
    return render(request, "winner/main.html")

def addTournament(request):
    if request.method == 'POST':
        tournamentForm = TournamentForm(request.POST)
        if tournamentForm.is_valid():
            level = tournamentForm.cleaned_data['level']
            tournament = tournamentForm.cleaned_data['tournament']
            gender = tournamentForm.cleaned_data['gender']
            date = tournamentForm.cleaned_data['date']
            venue = tournamentForm.cleaned_data['venue']
            p = Tournament(level=level, tournament=tournament, gender=gender, date=date, venue=venue)
            p.save()
            return render(request, "tournament/main.html")
        else:
            messages.error(request, "Error")
    else:
      tournamentForm = TournamentForm()

    return render(request, "tournament/add.html")

def addWinners(request):
    tournaments = Tournament.objects.all()
    context={
      'tournaments': tournaments
    }
    if request.method == 'POST':
        winnerForm = WinnerForm(request.POST)
        if winnerForm.is_valid():
            tournament = Tournament.objects.get(pk=winnerForm.cleaned_data['tournament'])
            gold = winnerForm.cleaned_data['gold']
            silver = winnerForm.cleaned_data['silver']
            bronze = winnerForm.cleaned_data['bronze']
            p = Winners(winners_for=tournament, gold=gold, silver=silver, bronze=bronze)
            p.save()
            return render(request, "winner/main.html")
        else:
            print(winnerForm.errors)
            messages.error(request, winnerForm.errors)
    else:
      winnerForm = WinnerForm()

    return render(request, "winner/add.html", context)

def editTournament(request, id):
    oldTournament = Tournament.objects.get(pk=id)
    if request.method == 'POST':
        tournamentForm = TournamentForm(request.POST)
        oldTournament.level = tournamentForm.data.get('level', None)
        oldTournament.tournament = tournamentForm.data.get('tournament', None)
        oldTournament.gender = tournamentForm.data.get('gender', None)
        oldTournament.date = tournamentForm.data.get('date', None)
        oldTournament.venue = tournamentForm.data.get('venue', None)
        oldTournament.save()
        return redirect("tournaments")
    else:
        tournamentForm = TournamentForm()
    return render(request, "tournament/edit.html", model_to_dict(oldTournament))

def editWinners(request, id):
    oldWinners = Winners.objects.get(pk=id)
    tournaments = Tournament.objects.all()
    context={
        'id': id,
        'oldWinners': oldWinners,
        'tournaments': tournaments
    }
    if request.method == 'POST':
        winnerForm = WinnerForm(request.POST)
        oldWinners.tournament = Tournament.objects.get(pk=winnerForm.data.get('tournament', None))
        oldWinners.gold = winnerForm.data.get('gold', None)
        oldWinners.silver = winnerForm.data.get('silver', None)
        oldWinners.bronze = winnerForm.data.get('bronze', None)
        oldWinners.save()
        return redirect("winners")
    else:
        winnerForm = WinnerForm()
    return render(request, "winner/edit.html", context)
    
def delTournament(request):
    if request.method == 'POST':
        Tournament.objects.get(pk=request.POST.get('id',None)).delete()
    return redirect("tournaments")
    
def delWinners(request):
    if request.method == 'POST':
        Winners.objects.get(pk=request.POST.get('id',None)).delete()
    return redirect("winners")