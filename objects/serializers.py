from rest_framework import serializers
from objects.models import Object

class ObjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Object
		fields = ('id', 'name')
