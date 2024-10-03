from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.exceptions import ValidationError


def validate_no_special_character(str):
    if(not str.isalnum()):
        raise ValidationError("Special character not allowed!")

def validate_string(str):
    if(not str.isdecimal()):
        raise ValidationError("Should include at least one non-digit character.")

class Author(models.Model):
    name = models.CharField(primary_key=True, max_length=100, unique=True, error_messages={ "unique": "Already used!" }, validators=[validate_string])
    password = models.CharField(name="password", max_length=100, blank=True, null=True)


class Star(models.Model):
     name = models.CharField(name="name", max_length=100, unique=True)
     owned_by = models.ForeignKey(Author, name="owned_by", blank=True, null=True, on_delete=models.SET_NULL, related_name="stars")
     planets_number = models.IntegerField(name="planets_number")
     spectral_type = models.CharField(name="spectral_type", max_length=100)
     effective_temp = models.FloatField(name="effective_temp")
     mass = models.FloatField(name="mass")
     radius = models.FloatField(name="radius")
     description = models.CharField(name="description", max_length=1000, blank=True, null=True)

    
class Planet(models.Model):
    name = models.CharField(name="name", max_length=100)
    semimajor_axis = models.FloatField(name="semimajor_axis")
    eccentricity = models.FloatField(name="eccentricity")
    mass = models.FloatField(name="mass")
    radius = models.FloatField(name="radius")
    magnetic_field = models.CharField(name="magnetic_field", blank=True, null=True, max_length=100)
    albedo = models.FloatField(name="albedo", blank=True, null=True)
    rotation_period = models.FloatField(name="rotation_period", blank=True, null=True)
    atmospheric_pressure = models.FloatField(name="atmospheric_pressure", blank=True, null=True)
    parent = models.ForeignKey(Star, name="parent", on_delete=models.CASCADE, related_name="planets")
    owned_by = models.ForeignKey(Author, name="owned_by", blank=True, null=True, on_delete=models.SET_NULL, related_name="planets")
    image = models.ImageField(blank=True, null=True)
    description = models.CharField(name="description", max_length=1000, blank=True, null=True)
    created_by_user = models.BooleanField(name="created_by_user", default=False)
    
    
class Quest(models.Model):
    number = models.IntegerField(name="number")
    name = models.CharField(name="name", max_length=100)
    description = models.CharField(name="description", max_length=1000)
    owned_by = models.ForeignKey(Author, name="owned_by", on_delete=models.CASCADE) 
    completed = models.BooleanField(name="completed")
    