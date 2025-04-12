from rest_framework import serializers
from.models import *

class ApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Apply
        fields = '__all__' # Предполагается, что поле 'name' содержит название жанра