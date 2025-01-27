from rest_framework import serializers
from .models import  Movie, Review, Director

class DirectorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Director
            fields = ('name',)

class MovieSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = ('title', 'description', 'duration', 'director')

class ReviewSerializer(serializers.ModelSerializer):

         class Meta:
             model = Review
             fields = ('text', 'movie')

