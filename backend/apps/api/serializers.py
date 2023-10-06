from rest_framework import serializers
from .models import Category, City, Advert


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['name']


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ['name']


class AdvertSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Advert
        fields = ['created', 'title', 'description', 'city', 'category', 'views']
