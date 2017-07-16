from django.forms import widgets
from rest_framework import serializers

from game_app.models import *
from django.contrib.auth.models import User


class RefereeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referee
        fields = '__all__'
