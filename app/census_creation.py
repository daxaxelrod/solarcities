import pandas as pd
path = "/Users/davidaxelrod/Documents/solarcities/census.csv"

# Make a row iterator (this will go row by row)

from app import models
head = True
escapes = ''.join([chr(char) for char in range(1, 32)])

with open(path, 'rb') as f:
  for line in f:
      if not head:
          data=str(line).split(",")
          print("{} {} {}".format(data[8], data[9], data[17]))
          models.City.objects.create(name=data[8], state=data[9], population=data[17])
      else:
          head=False
