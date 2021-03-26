from django.urls import include, path
from users.views import dashboard, register, tournaments, addTournament, editTournament, TournamentJson

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("", dashboard, name="dashboard"),
    path("register/", register, name="register"),
    path("tournaments/", tournaments, name="tournaments"),
    path("add/tournament/", addTournament, name="add_tournaments"),
    path("edit/<int:id>/tournament/", editTournament, name="edit_tournaments"),

    path("getTournament/", TournamentJson.as_view(), name='getTournament'),
]
