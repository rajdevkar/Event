from django.urls import include, path
from users.views import dashboard, register, tournaments, winners, addTournament, addWinners, editTournament, editWinners, delTournament, delWinners, TournamentJson, WinnerJson

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("", dashboard, name="dashboard"),
    path("register/", register, name="register"),

    # TOURNAMENT
    path("tournaments/", tournaments, name="tournaments"),
    path("add/tournament/", addTournament, name="add_tournaments"),
    path("edit/<int:id>/tournament/", editTournament, name="edit_tournaments"),
    path("tournament/delete", delTournament, name="delete_tournament"),

    # WINNER
    path("winners/", winners, name="winners"),
    path("add/winners/", addWinners, name="add_winners"),
    path("edit/<int:id>/winners/", editWinners, name="edit_winners"),
    path("winners/delete", delWinners, name="delete_winners"),

    path("getTournament/", TournamentJson.as_view(), name='getTournament'),
    path("getWinners/", WinnerJson.as_view(), name='getWinners'),
]
