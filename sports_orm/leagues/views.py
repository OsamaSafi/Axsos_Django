from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		# "leagues": League.objects.all(),
		# "teams": Team.objects.all(),
		# "players": Player.objects.all(),
		"leagues" : League.objects.filter(sport="Baseball"),
		"leagues" : League.objects.filter(name__contains="Women"),
		"leagues" : League.objects.filter(sport__contains="Hockey"),
		"leagues" : League.objects.exclude(sport="Football"),
		"leagues" : League.objects.filter(name__icontains="conference"),
		"leagues" : League.objects.filter(name__icontains="Atlantic"),
		"teams" : Team.objects.filter(location="Dallas"),
		"teams" : Team.objects.filter(team_name="Raptors"),
		"teams" : Team.objects.filter(location__icontains="city"),
		"teams" : Team.objects.filter(team_name__startswith="T"),
		"teams" : Team.objects.all().order_by('location'),
		"teams" : Team.objects.all().order_by('-team_name'),
		"teams" : Team.objects.all().order_by('-team_name'),
		"players": Player.objects.filter(last_name='Cooper'),
		"players": Player.objects.filter(first_name__contains='Joshua'),
		"players": Player.objects.filter(last_name='Cooper').exclude(first_name='Joshua'),
		"players": Player.objects.filter(first_name__in=['Alexander','Wyatt']),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")