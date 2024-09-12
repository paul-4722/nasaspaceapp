from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.exceptions import ValidationError


def validate_no_special_character(str):
    if(not str.isalnum()):
        raise ValidationError("Special character not allowed!")
    

class Author(models.Model):
    name = models.CharField(primary_key=True, max_length=100, unique=True, error_messages={ "unique": "Already used!" }, validators=[validate_no_special_character])


class Star(models.Model):
     name = models.CharField(name="name", max_length=100, unique=True, validators=[validate_no_special_character])
     size = models.FloatField(name="size")
     owned_by = models.ForeignKey(Author, name="owned_by", blank=True, null=True, on_delete=models.SET_NULL, related_name="stars")

    
class Planet(models.Model):
    name = models.CharField(name="name", max_length=100, validators=[validate_no_special_character])
    size = models.FloatField(name="size")
    parent = models.ForeignKey(Star, name="parent", on_delete=models.CASCADE, related_name="planets")
    owned_by = models.ForeignKey(Author, name="owned_by", blank=True, null=True, on_delete=models.SET_NULL, related_name="planets")