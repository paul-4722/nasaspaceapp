from rest_framework import serializers
from .models import Author, Planet, Star


class AuthorSerializer(serializers.ModelSerializer):
    name = serializers.CharField(allow_null=True)
    class Meta:
        model = Author
        fields = ["name"]


class AuthorPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["name"]


class PlanetSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = ["name", "size", "image"]


class PlanetDetailedGetSerializer(serializers.ModelSerializer):
    class StarSerializer(serializers.ModelSerializer):
        class Meta:
            model = Star
            fields = ["name"]
    parent = StarSerializer()
    class Meta:
        model = Planet
        fields = ["name", "size", "parent", "owned_by", "image"]
        
        
class PlanetDetailedPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = ["name", "size", "image"]


class StarSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Star
        fields = ["name", "size", "owned_by"]


class StarDetailedGetSerializer(serializers.ModelSerializer):
    planets = PlanetSimpleSerializer(many=True, read_only=True)
    owned_by = AuthorSerializer()
    class Meta:
        model = Star
        fields = ["name", "size", "owned_by", "planets"]


class StarDetailedPostSerializer(serializers.ModelSerializer):
    owned_by = AuthorSerializer()
    class Meta:
        model = Star
        fields = ["owned_by"]