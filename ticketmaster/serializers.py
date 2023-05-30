from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        # fields = ['keyword','category','distance','location']
        fields= "__all__"