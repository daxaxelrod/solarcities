from django.shortcuts import render
import math
import numpy as np


KWH_PH = 901*12
PANEL_OUTPUT = .255
PRICE_PER_PANEL = 250
TURBINE_OUTPUT = 100 #in kwh running for a year
PRICE_PER_TURBINE = 6500 * TURBINE_OUTPUT

def map(request):

    location = {"average_sun_per_day": 6, "average_wind_per_day": 6, "population": 1}

    pop = getPop()
    num_houses = pop / 3
    tot_nrg = KWH_PH * num_houses

    single_panel_potential = location["average_sun_per_day"] * PANEL_OUTPUT * 365
    single_wind_potential = location["average_wind_per_day"] * TURBINE_OUTPUT * 365

    num_solar_panels = math.ceil(tot_nrg / single_panel_potential)
    num_wind_turbines = math.ceil(tot_nrg / single_wind_potential)
    total_cost = PRICE_PER_PANEL * num_solar_panels + num_wind_turbines * PRICE_PER_TURBINE # always going to be absurd
    best_num_panels = 0
    best_num_turbines = 0



    for i in np.arange(0,101,10):
        print("________")
        print((1- (i/100)))
        print("________")
        '''
        proposed_cost = (PRICE_PER_PANEL * (i/100) * num_solar_panels) + (PRICE_PER_TURBINE * (1- (i/100)) * num_wind_turbines)
        print("best panels: {}".format(best_num_panels))
        print("best turbines: {}".format(best_num_turbines))
        print("best proposed_cost {}".format(proposed_cost))
        if proposed_cost < total_cost:
            total_cost = proposed_cost
            best_num_panels = (i/100) * num_solar_panels
            best_num_turbines = (1-(i/100)) * num_wind_turbines
        '''
        proposed_cost = (PRICE_PER_PANEL * (1-(i/100.0)) * num_solar_panels) + (PRICE_PER_TURBINE * ((i/100.0)) * num_wind_turbines)
        print("best panels: {}".format(best_num_panels))
        print("best turbines: {}".format(best_num_turbines))
        print("best proposed_cost {}".format(proposed_cost))
        if proposed_cost < total_cost:
            total_cost = proposed_cost
            best_num_panels = (1-(i/100.0)) * num_solar_panels
            best_num_turbines = ((i/100.0)) * num_wind_turbines

    return render(request, "map.html", {"num_turbines": best_num_turbines, "num_panels": best_num_panels, "total_cost": total_cost})


def getPop():
    return 300000
