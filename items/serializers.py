from rest_framework import serializers
from items.models import Item
from django.contrib.auth.models import User

class ItemSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	
	class Meta:
		model = Item
		fields = ('id', 'name', 'owner')

class UserSerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(many=True, queryset=Item.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'items')