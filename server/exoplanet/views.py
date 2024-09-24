from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import get_object_or_404
from django.contrib.auth import authenticate, login, logout

from .models import Author, Star, Planet
import exoplanet.serializers as serializers



class LandingView(generics.GenericAPIView):
    def get(self, request):
        return Response(status=status.HTTP_200_OK)


class PlanetListView(generics.GenericAPIView):
    def get_queryset(self):
        return Planet.objects.all()

    def get(self, request):
        planets = self.get_queryset()
        serializer = serializers.PlanetDetailedGetSerializer(planets, many=True)
        return Response({"planets":serializer.data}, status=status.HTTP_200_OK)


class StarListView(generics.GenericAPIView):
    def get_queryset(self):
        return Star.objects.all()

    def get(self, request):
        stars = self.get_queryset()
        serializer = serializers.StarDetailedGetSerializer(stars, many=True)
        return Response({"stars":serializer.data}, status=status.HTTP_200_OK)


class StarDetailedView(generics.GenericAPIView):
    serializer_class = serializers.StarDetailedPostSerializer
    
    def get_object(self, pk):
        return get_object_or_404(Star, pk=pk)
    
    def get(self, request, pk):
        star = self.get_object(pk)  
        serializer = serializers.StarDetailedGetSerializer(star)
        return Response({"star":serializer.data})

    def post(self, request, pk):
        star = self.get_object(pk)
        print(request.data)
        user_name = request.data["owned_by.name"]
        if star.owned_by:
            owner_name = star.owned_by.name
            if owner_name == user_name:
                serializer = serializers.StarDetailedGetSerializer(star)
                return Response({"star":serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"message":"Cannot change owner of the star."}, status=status.HTTP_403_FORBIDDEN)
        else:
            if Author.objects.filter(name=user_name).count() == 0:
                Author.objects.create(name=user_name)
            author = Author.objects.filter(name=user_name)[0]
            serializer = serializers.StarDetailedGetSerializer(star, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save(owned_by=author)
                return Response({"star":serializer.data}, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)


class PlanetCreateView(generics.GenericAPIView):
    serializer_class = serializers.PlanetDetailedPostSerializer
    
    def get_object(self, pk):
        return get_object_or_404(Star, pk=pk)
    
    def get(self, request, pk):
        star = self.get_object(pk)  
        serializer = serializers.StarSimpleSerializer(star)
        return Response({"star":serializer.data})
    
    def post(self, request, pk):
        star = self.get_object(pk)
        serializer = serializers.PlanetDetailedPostSerializer(data=request.data)
        author = star.owned_by
        if author:
            if serializer.is_valid():
                serializer.save(owned_by=author, parent=star)
                return Response({"planet": serializer.data}, status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"message":"No owner of this star."}, status=status.HTTP_404_NOT_FOUND)
        
    
    
class PlanetDetailedView(generics.GenericAPIView):
    
    def get_object(self, pk):
        planet = get_object_or_404(Planet, pk=pk)
        return planet
    
    def get(self, request, pk):
        planet = self.get_object(pk)
        serializer = serializers.PlanetDetailedGetSerializer(planet)
        return Response({"planet":serializer.data}, status=status.HTTP_200_OK)
    

    
    