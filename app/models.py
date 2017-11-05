from django.db import models

# Create your models here.
class City(models.Model):
    state = models.CharField(max_length=50)
    name = models.CharField(max_length=150)
    #2016
    population = models.IntegerField()

    def __str__(self):
        return "{}, {}".format(self.name, self.state)
