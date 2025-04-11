from rest_framework import serializers
from .models import Tour, Rating

class RatingSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')  # Автоматически подставим user из request

    class Meta:
        model = Rating
        fields = ['id', 'user', 'tour', 'score', 'comment', 'created_at']
        read_only_fields = ['created_at']

    def validate_score(self, value):
        if not (1.0 <= value <= 5.0):
            raise serializers.ValidationError("Оценка должна быть от 1.0 до 5.0")
        return value

    def create(self, validated_data):
        user = self.context['request'].user
        tour = validated_data['tour']
        rating, created = Rating.objects.update_or_create(
            user=user,
            tour=tour,
            defaults={'score': validated_data['score'], 'comment': validated_data.get('comment', '')}
        )
        return rating


class TourSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    ratings_count = serializers.SerializerMethodField()

    class Meta:
        model = Tour
        fields = '__all__'  # или перечисли поля вручную
        read_only_fields = ['average_rating', 'ratings_count']

    def get_average_rating(self, obj):
        return obj.average_rating()

    def get_ratings_count(self, obj):
        return obj.ratings.count()


"""Келечекте бул файл өзгөрүш мүмкүн"""