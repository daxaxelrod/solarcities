from django.shortcuts import render
from django.http import JsonResponse

from . import models
import math
import numpy as np


KWH_PH = 901*12
PANEL_OUTPUT = .255
PRICE_PER_PANEL = 250
TURBINE_OUTPUT = 3000 #in kwh running for a year
PRICE_PER_TURBINE = 3274490.00

def map(request):
    return render(request, "map.html")

tot_nrg = 0
# could use django rest framework in the future
def calc(request):
    city = request.GET.get("city")
    state = request.GET.get("state")
    avg_sun_pd = float(request.GET.get("sun_year_hours"))/365.0
    avg_wind_pd = float(request.GET.get("wind_year_hours"))/365.0
    pop = getPop(city, state)

    location = {"average_sun_per_day": avg_sun_pd,
                "average_wind_per_day": avg_wind_pd,
                "population": pop}
    num_houses = pop / 3
    tot_nrg = KWH_PH * num_houses

    single_panel_potential = location["average_sun_per_day"] * PANEL_OUTPUT * 365
    single_wind_potential = location["average_wind_per_day"] * TURBINE_OUTPUT * 365

    num_solar_panels = math.ceil(tot_nrg / single_panel_potential)
    num_wind_turbines = math.ceil(tot_nrg / single_wind_potential)
    total_cost = PRICE_PER_PANEL * num_solar_panels + num_wind_turbines * PRICE_PER_TURBINE # always going to be absurd
    best_num_panels = 0
    best_num_turbines = 0

    solar_to_wind = []
    get_wind = lambda num_solar: (tot_nrg - (num_solar * single_panel_potential)) / single_wind_potential
    get_solar = lambda num_wind: (tot_nrg - (num_wind * single_wind_potential)) / single_panel_potential

    for s in range(int(num_solar_panels)):
        solar_to_wind.append([s, get_wind(s)])

    for w in range(int(num_wind_turbines)):
        solar_to_wind.append([get_solar(w), w])

    for (s, w) in solar_to_wind:
        proposed_cost = (PRICE_PER_PANEL * s) + (PRICE_PER_TURBINE * w)

        if proposed_cost < total_cost:
            total_cost = proposed_cost
            best_num_panels = s
            best_num_turbines = w

    wind_factor = 10
    solar_factor = 1000
    return JsonResponse({   "num_turbines": best_num_turbines,
                            "num_panels": best_num_panels,
                            "total_cost": round(total_cost, 2),
                            "turbine_factor": wind_factor,
                            "solar_factor": solar_factor})



def getPop(city_name, state):
    city = models.City.objects.filter(name__icontains=city_name, state__icontains=state).first()
    try:
        return city.population
    except Exception:
        return 100000
