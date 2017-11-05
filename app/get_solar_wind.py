import re
import numpy as np
s = open('solar.txt', 'r')
w = open('wind.txt', 'r')

def get_wind_hours(mean):
    sigma = mean / 2
    w_speeds = np.random.normal(mean, sigma, 8760)
    return len([x for x in w_speeds if x <= 55 and x >= 8])

cities = []
with open('cities.txt', 'r') as f:
    cities = f.read().splitlines()

with open('city_solar_wind.txt', 'w') as f:
    for sol, wind in zip(s.readlines(), w.readlines()):
        city = sol[:sol.find(',')]
        print city
        if city not in cities:
            continue
        sunny_hours = int(sol.split()[-2])
        windy_hours = get_wind_hours(float(wind.split()[-2]))
        print sunny_hours
        print windy_hours
        f.write(city + ' ' + str(sunny_hours) + ' ' + str(windy_hours) + '\n')


s.close()
w.close()
