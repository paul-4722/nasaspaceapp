from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404

from .quests import quests
from .models import Author, Star, Planet, Quest
import exoplanet.serializers as serializers
import random



class LandingView(generics.GenericAPIView):
    def get(self, request):
        return Response(status=status.HTTP_200_OK)



class StarListView(generics.GenericAPIView):
    def get_queryset(self):
        return Star.objects.filter(show=1)

    def get(self, request):
        stars = self.get_queryset()
        serializer = serializers.StarSimpleSerializer(stars, many=True)
        return Response({"stars":serializer.data}, status=status.HTTP_200_OK)


class StarDetailedView(generics.GenericAPIView):
    serializer_class = serializers.AuthorPostSerializer
    
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
                points = quest["points"], 
                type = quest["type"], 
                target = quest["target"], 
                progress = 0, 
                owned_by = author, 
            ) 
    
    def post(self, request, pk):
        star = self.get_object(pk)
        user_name = request.data["name"]
        user_password = request.data["password"]
        if star.owned_by:
            return Response({"message":"Cannot change owner of the star."}, status=status.HTTP_403_FORBIDDEN)
        else:
            if Author.objects.filter(name=user_name).count() == 0:
                if len(user_name.split(" ")) > 1 or len(user_name) == 0 or user_name.isdigit():
                    return Response(status=status.HTTP_404_NOT_FOUND)
                Author.objects.create(name=user_name, password=user_password)
                author = Author.objects.filter(name=user_name)[0]
                self.make_quest(author)
                star.owned_by = author
                star.save()
                serializer = serializers.StarDetailedGetSerializer(star)          
                return Response({"star":serializer.data}, status=status.HTTP_202_ACCEPTED)
            else:
                return Response({"message":"Already used name. "}, status=status.HTTP_403_FORBIDDEN)


class StarDetailedViewByAuthor(generics.GenericAPIView):
    
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
    
    def get_object_star(self, id):
        star = get_object_or_404(Star, pk=id)
        return star
    
    def get(self, request, pk):
        planet = self.get_object(pk)
        serializer = serializers.PlanetDetailedGetSerializer(planet)
        return Response({"planet":serializer.data}, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        planet = self.get_object(pk)
        star_id = planet.parent.id
        star = self.get_object_star(star_id)
        star.planets_number -= 1
        star.save()
        planet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OriginStarRandomView(generics.GenericAPIView):
    
    def get_queryset(self):
        stars = Star.objects.filter(show=0)
        return stars
    
    def get_random(self, stars):
        len = stars.count()
        ran = random.randint(0, len-1)
        return ran
    
    def get(self, request):
        stars = self.get_queryset()
        ran = self.get_random(stars)
        serializer = serializers.StarSimpleSerializer(stars[ran])
        return Response({"star":serializer.data})


class UserStarRandomView(generics.GenericAPIView):
    
    def get_queryset(self, name):
        stars = Star.objects.filter(owned_by__isnull=False).exclude(owned_by__name=name)
        return stars
    
    def get_random(self, stars):
        len = stars.count()
        ran1 = random.randint(0, len-1)
        ran2 = random.randint(0, len-1)
        while ran1 == ran2: ran2 = random.randint(0, len-1)
        return (ran1, ran2)
    
    def get(self, request, name):
        stars = self.get_queryset(name)
        ran1, ran2 = self.get_random(stars)
        serializer1 = serializers.StarSimpleSerializer(stars[ran1])
        serializer2 = serializers.StarSimpleSerializer(stars[ran2])
        return Response({"star1":serializer1.data, "star2":serializer2.data})


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
    def get_object_quest(self, name, number):
        return Quest.objects.get(owned_by=name, number=number)

    def get_object_author(self, name):
        return Author.objects.get(name=name)
    
    def post(self, request, name, number):
        quest = self.get_object_quest(name, number)
        quest.progress += 1
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
        newpoint = author.points + int(request.data["points"])
        serializer = serializers.PointsGetSerializer(author)
        if newpoint < 0:
            return Response(status=status.HTTP_403_FORBIDDEN)
        else:
            author.points = newpoint
            author.save()
            return Response({"user": serializer.data}, status=status.HTTP_200_OK)


class AuthView(generics.GenericAPIView):
    serializer_class = serializers.AuthorPostSerializer
    def get_object(self, name):
        return get_object_or_404(Author, name=name)
    
    def post(self, request):
        author = self.get_object(request.data["name"])
        if author.password == request.data["password"]:
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
    