from django.urls import path
from .views import SentimentPredictionAPIView

urlpatterns = [
    path('predict_sentiment/', SentimentPredictionAPIView.as_view(),
         name='predict_sentiment'),
]
