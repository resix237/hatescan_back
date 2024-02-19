from rest_framework import serializers
from .models import SentimentPrediction


class SentimentPredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SentimentPrediction
        fields = ['text', 'sentiment']
