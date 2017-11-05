solar = []
with open('solar.txt', 'r') as f:
    for line in f:
        solar.append(line[:line.find(',')])

wind = []
with open('wind.txt', 'r') as f:
    for line in f:
        wind.append(line[:line.find(',')])

cities = set(solar) & set(wind)
print set(solar) - set(wind)
print set(wind) - set(solar)

with open('cities.txt', 'w') as f:
    for city in cities:
        f.write("%s\n" % city)
