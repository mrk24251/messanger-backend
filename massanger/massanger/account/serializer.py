from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers

from massage.models import Massanger


class Searchserializer(serializers.Serializer):
	username = serializers.CharField()

class Massangerserializer(serializers.ModelSerializer):
	class Meta:
		model = Massanger
		fields = '__all__'