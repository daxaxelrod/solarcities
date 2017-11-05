from django.contrib import admin

from . import models
# Register your models here.
class CityAdmin(admin.ModelAdmin):

    search_fields = ['name', "population"]

admin.site.register(models.City, CityAdmin)
