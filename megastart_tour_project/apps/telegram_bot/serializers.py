from rest_framework import serializers
from megastart_tour_project.apps.telegram_bot.database.models import *

class ApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Apply
        fields = '__all__' # Предполагается, что поле 'name' содержит название жанра