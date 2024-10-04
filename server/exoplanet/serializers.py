from rest_framework import serializers
from .models import Author, Planet, Star, Quest


class AuthorSerializer(serializers.ModelSerializer):
    name = serializers.CharField(allow_null=True)
    class Meta:
        model = Author
        fields = ["name", "password"]


class AuthorPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["name", "password"]


class PlanetSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = ["id", "name", "image"]


class PlanetDetailedGetSerializer(serializers.ModelSerializer):
    class StarSerializer(serializers.ModelSerializer):
        class Meta:
            model = Star
            fields = ["name"]
    parent = StarSerializer()
    class Meta:
        model = Planet
        fields = ["id", "name", "parent", "owned_by", "created_by_user", "image", "semimajor_axis", "eccentricity", "mass", "radius", "magnetic_field", "albedo", "rotation_period", "atmospheric_pressure", "description"]
        
        
class PlanetDetailedPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = ["name", "image", "semimajor_axis", "eccentricity", "mass", "radius", "magnetic_field", "albedo", "rotation_period", "atmospheric_pressure", "description"]


class StarSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Star
        fields = ["id", "name", "owned_by", "azi", "pol"]


class StarDetailedGetSerializer(serializers.ModelSerializer):
    planets = PlanetSimpleSerializer(many=True, read_only=True)
    owned_by = AuthorSerializer()
    class Meta:
        model = Star
        fields = ["name", "owned_by", "azi", "pol", "dist", "planets_number", "spectral_type", "effective_temp", "mass", "radius", "description", "planets"]


class StarDetailedPostSerializer(serializers.ModelSerializer):
    owned_by = AuthorSerializer()
    class Meta:
        model = Star
        fields = ["owned_by"]


class QuestGetSerializer(serializers.ModelSerializer):
    owned_by = AuthorSerializer()
    class Meta:
        model = Quest
        fields = ["number", "name", "owned_by", "completed", "description"]


class QuestPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quest
        fields = [""]


class PointsGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["name", "points"]


class PointsPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["points"]