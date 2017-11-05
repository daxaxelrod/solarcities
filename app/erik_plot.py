import math
import numpy as np
import sys
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def getPop():
    return 300

def get_solar(num_wind):
    return  (tot_nrg - (num_wind * single_wind_potential)) / single_panel_potential

def get_wind(num_solar):
    return  (tot_nrg - (num_solar * single_panel_potential)) / single_wind_potential

KWH_PH = 901*12
PANEL_OUTPUT = .255
PRICE_PER_PANEL = 250
TURBINE_OUTPUT = 3000 #in kwh running for a year
PRICE_PER_TURBINE = 3274490.00

results = {}
best_cost = []
best_solar = []
best_wind = []

x = []
y = []
for i in range(1,25):
    for j in range(1,25):
        location = {"average_sun_per_day": i, "average_wind_per_day": j, "population": 1}

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

        solar_to_wind = []
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

        print ("i: ", i, "j: ", j)
        print ("Cost: ", total_cost)
        best_cost.append(total_cost)
        print ("Num_solar: ", best_num_panels * .255)
        best_solar.append(best_num_panels)
        print ("Num_wind: ", best_num_turbines)
        best_wind.append(best_num_turbines * 3000)
        x.append(i)
        y.append(j)
#print ("All wind:
mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(x,y, best_solar, label='Best Solar')
ax.plot(x,y, best_wind, label='Best Wind')

ax.set_xlabel("Hours of sun per day")
ax.set_ylabel("Hours of wind per day")
ax.legend()
plt.show()
