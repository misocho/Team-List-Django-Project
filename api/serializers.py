from rest_framework import serializers
from .models import TeamList

class TeamListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TeamList
        fields = ('id', 'firstname', 'lastname')