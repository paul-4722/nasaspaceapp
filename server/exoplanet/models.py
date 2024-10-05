from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.exceptions import ValidationError


def validate_no_special_character(str):
    if(not str.isalnum()):
        raise ValidationError("Special character not allowed!")

def validate_string(str):
    if(str.isdecimal()):
        raise ValidationError("Should include at least one non-digit character.")

class Author(models.Model):
    name = models.CharField(primary_key=True, max_length=100, unique=True, error_messages={ "unique": "Already used!" }, validators=[validate_string])
    password = models.CharField(name="password", max_length=100, blank=True, null=True)
    points = models.IntegerField(name="points", default=0)


class Star(models.Model):
    name = models.CharField(name="name", max_length=100, unique=True)
    planets_number = models.IntegerField(name="planets_number")
    spectral_type = models.CharField(name="spectral_type", max_length=100, blank=True, null=True)
    effective_temp = models.FloatField(name="effective_temp", blank=True, null=True)
    radius = models.FloatField(name="radius", blank=True, null=True)
    mass = models.FloatField(name="mass", blank=True, null=True)
    luminosity = models.FloatField(name="luminosity", blank=True, null=True)
    azi = models.FloatField(name="azi", default=0)
    pol = models.FloatField(name="pol", default=0)
    visual_magnitude = models.FloatField(name="visual_magnitude", blank=True, null=True)
    habitable_min = models.FloatField(name="habitable_min", blank=True, null=True)
    habitable_max = models.FloatField(name="habitable_max", blank=True, null=True)
    
    owned_by = models.ForeignKey(Author, name="owned_by", blank=True, null=True, on_delete=models.SET_NULL, related_name="stars")
    description = models.CharField(name="description", max_length=1000, blank=True, null=True)

    
class Planet(models.Model):
    
    # data
    name = models.CharField(name="name", max_length=100)
    semimajor_axis = models.FloatField(name="semimajor_axis", blank=True, null=True)
    radius = models.FloatField(name="radius", blank=True, null=True)
    mass = models.FloatField(name="mass", blank=True, null=True)
    density = models.FloatField(name="density", blank=True, null=True)
    eccentricity = models.FloatField(name="eccentricity", default=0)
    insolation = models.FloatField(name="insolation", blank=True, null=True)
    temperature = models.FloatField(name="temperature", blank=True, null=True)
    escape_vel = models.FloatField(name="escape_vel", blank=True, null=True)
    ESI = models.FloatField(name="ESI", blank=True, null=True)
    SType = models.CharField(name="SType", max_length=10)
    TType = models.CharField(name="TType", max_length=10)
    parent = models.ForeignKey(Star, name="parent", on_delete=models.CASCADE, related_name="planets")
    
    description = models.CharField(name="description", max_length=1000, blank=True, null=True)
    
    # user
    magnetic_field = models.CharField(name="magnetic_field", blank=True, null=True, max_length=100)
    albedo = models.FloatField(name="albedo", blank=True, null=True)
    rotation_period = models.FloatField(name="rotation_period", blank=True, null=True)
    atmospheric_pressure = models.FloatField(name="atmospheric_pressure", blank=True, null=True)
    atmospheric_composition = models.CharField(name="atmospheric_composition", max_length=100, blank=True, null=True)
    
    
    owned_by = models.ForeignKey(Author, name="owned_by", blank=True, null=True, on_delete=models.SET_NULL, related_name="planets")
    image = models.ImageField(blank=True, null=True)
    
    created_by_user = models.BooleanField(name="created_by_user", default=False)
    
    
class Quest(models.Model):
    number = models.IntegerField(name="number")
    name = models.CharField(name="name", max_length=100)
    description = models.CharField(name="description", max_length=1000)
    owned_by = models.ForeignKey(Author, name="owned_by", on_delete=models.CASCADE) 
    #points = models.IntegerField(name="points")
    completed = models.BooleanField(name="completed")
    