from .models import Country
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"