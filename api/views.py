from rest_framework import viewsets
from api.serializers import TeamListSerializer
from api.models import TeamList

class TeamListView(viewsets.ModelViewSet):
    queryset = TeamList.objects.all()
    serializer_class = TeamListSerializer