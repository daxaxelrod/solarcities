from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.map, name="map"),
    url(r'^panels_and_turbines/$', views.calc, name="calculations")
]
