from rest_framework import serializers
from .models import Author, Planet, Star, Quest


class AuthorSerializer(serializers.ModelSerializer):
    name = serializers.CharField(allow_null=True)
    class Meta:
        model = Author
        fields = ["name"]


class AuthorPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["name", "password"]


class PlanetSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = ["id", "name", "semimajor_axis", "eccentricity", "radius", "image", "SType", "TType"]


class PlanetDetailedGetSerializer(serializers.ModelSerializer):
    class StarSerializer(serializers.ModelSerializer):
        class Meta:
            model = Star
            fields = ["id", "name"]
    parent = StarSerializer()
    class Meta:
        model = Planet
        exclude = []        
        
class PlanetDetailedPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        exclude = ["parent", "owned_by", "created_by_user"]


class StarSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Star
        fields = ["id", "name", "owned_by", "azi", "pol"]


class StarDetailedGetSerializer(serializers.ModelSerializer):
    planets = PlanetSimpleSerializer(many=True, read_only=True)
    owned_by = AuthorSerializer()
    class Meta:
        model = Star
        exclude = []    


class QuestGetSerializer(serializers.ModelSerializer):
    owned_by = AuthorSerializer()
    class Meta:
        model = Quest
        fields = ["number", "name", "owned_by", "completed", "description"]


class QuestPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quest
        fields = []


class PointsGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["name", "points"]


class PointsPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["points"]


class ScenariosGetSerializer(serializers.ModelSerializer):
    scenarios = serializers.ListField(child=serializers.IntegerField())

    class Meta:
        model = Author
        fields = ["name", "scenarios"]


class ScenariosPostSerializer(serializers.ModelSerializer):
    scenario = serializers.IntegerField()
