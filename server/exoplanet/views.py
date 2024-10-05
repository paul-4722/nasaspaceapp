from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404

from .quests import quests
from .models import Author, Star, Planet, Quest
import exoplanet.serializers as serializers



class LandingView(generics.GenericAPIView):
    def get(self, request):
        return Response(status=status.HTTP_200_OK)



class StarListView(generics.GenericAPIView):
    def get_queryset(self):
        return Star.objects.all()

    def get(self, request):
        stars = self.get_queryset()
        serializer = serializers.StarSimpleSerializer(stars, many=True)
        return Response({"stars":serializer.data}, status=status.HTTP_200_OK)


class StarDetailedView(generics.GenericAPIView):
    serializer_class = serializers.StarDetailedPostSerializer
    
    def get_object(self, pk):
        return get_object_or_404(Star, pk=pk)
    
    def get(self, request, pk):
        star = self.get_object(pk)  
        serializer = serializers.StarDetailedGetSerializer(star)
        return Response({"star":serializer.data})

    def make_quest(self, author):
        for quest in quests:
            Quest.objects.create(
                name = quest["name"], 
                description = quest["description"], 
                number = quest["number"], 
                owned_by = author, 
                completed = False
            ) 
    
    def post(self, request, pk):
        star = self.get_object(pk)
        user_name = request.data["owned_by.name"]
        user_password = request.data["owned_by.password"]
        if star.owned_by:
            return Response({"message":"Cannot change owner of the star."}, status=status.HTTP_403_FORBIDDEN)
        else:
            if Author.objects.filter(name=user_name).count() == 0:
                Author.objects.create(name=user_name, password=user_password)
                author = Author.objects.filter(name=user_name)[0]
                serializer = serializers.StarDetailedGetSerializer(star, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save(owned_by=author)
                    self.make_quest(author)
                    return Response({"star":serializer.data}, status=status.HTTP_202_ACCEPTED)
                else:
                    return Response(status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({"message":"Already used name. "}, status=status.HTTP_403_FORBIDDEN)


class StarDetailedViewByAuthor(generics.GenericAPIView):
    serializer_class = serializers.StarDetailedPostSerializer
    
    def get_object(self, name):
        author = get_object_or_404(Author, name=name)
        return get_object_or_404(Star, owned_by=author)
    
    def get(self, request, name):
        star = self.get_object(name)  
        serializer = serializers.StarDetailedGetSerializer(star)
        return Response({"star":serializer.data})
        

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
                serializer.save(owned_by=author, parent=star, created_by_user=True)
                star.planets_number += 1
                star.save()
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


class QuestListView(generics.GenericAPIView):
    
    def get_queryset(self, name):
        author = get_object_or_404(Author, name=name)
        return Quest.objects.filter(owned_by=author)
    
    def get(self, request, name):
        quests = self.get_queryset(name)
        serializer = serializers.QuestGetSerializer(quests, many=True)
        return Response({"quests":serializer.data}, status=status.HTTP_200_OK)
    

class QuestCompleteView(generics.GenericAPIView):
    serializer_class = serializers.QuestPostSerializer
    def get_object(self, name, number):
        return Quest.objects.get(owned_by=name, number=number)
    
    def post(self, request, name, number):
        quest = self.get_object(name, number)
        quest.completed = True
        quest.save()
        return Response(status=status.HTTP_200_OK)
    

class PointsView(generics.GenericAPIView):
    serializer_class = serializers.PointsPostSerializer
    def get_object(self, name):
        return get_object_or_404(Author, name=name)
    
    def get(self, request, name):
        author = self.get_object(name)
        serializer = serializers.PointsGetSerializer(author)
        return Response({"user": serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request, name):
        author = self.get_object(name)
        serializer = serializers.PointsGetSerializer(instance=author, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"user": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        