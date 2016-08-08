from objects.models import Object
from objects.serializers import ObjectSerializer
from rest_framework import generics

class ObjectList(generics.ListCreateAPIView):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer


class ObjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer
