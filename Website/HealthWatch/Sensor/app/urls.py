from django.urls import path
from app import views

urlpatterns = [
    path("about_us", views.about_us, name="about_us"),
    path("body_temp", views.body_temp, name="body_temp"),
    path("env_temp", views.env_temp, name="env_temp"),
    path("gases", views.gases, name="gases"),
    path("location", views.location, name="location"),
    path("pulse_rate", views.pulse_rate, name="pulse_rate"),
    path("spO2", views.spO2, name="spO2"),
    path("", views.env_temp, name="env_temp"),
]
