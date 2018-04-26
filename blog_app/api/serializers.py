from rest_framework import  serializers
from blog_app.models import Trip, AuthUser

class TripListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ('date','title')

class TripDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ('date','title','details')

class TripCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trip
        fields = ('date','title','details')

"""

data = {
    "title":"My trip to India",
    "date":"2017-03-11",
    "details":"<p>:)</p>",
    "id": "35",
}

new_item = TripSerializer(data=data)
if new_item.is_valid():
    new_item.save()
else:
    print(new_item.errors)

"""
