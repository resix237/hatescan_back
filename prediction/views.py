from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import SentimentPrediction
from .serializers import SentimentPredictionSerializer
import joblib


import os

current_directory = os.path.abspath(os.path.dirname(__file__))
vectorizer_path = os.path.join(current_directory, 'modeles', 'vectorizer.pkl')
model_path = os.path.join(current_directory, 'modeles', 'nb_model.pkl')

# Exemple d'utilisation d'un modèle de prédiction de sentiment (à adapter selon votre modèle)


def predict_sentiment(text):
    vectorizer = joblib.load(vectorizer_path)
    loaded_svm_model = joblib.load(model_path)
    vectorized_text = vectorizer.transform([text])
    prediction = loaded_svm_model.predict(vectorized_text)
    # Convertir le résultat de la prédiction en 'Positif' ou 'Négatif' (à adapter)
    sentiment = 'Sms Légitime' if prediction[0] == 1 else 'Spam'

    return sentiment


class SentimentPredictionAPIView(APIView):
    def post(self, request, *args, **kwargs):
        text = request.data.get('text', '')
        # Effectuer la prédiction
        sentiment = predict_sentiment(text)
        # Sauvegarder la prédiction dans la base de données
        prediction_data = {'text': text, 'sentiment': sentiment}
        return Response({'sentiment': sentiment}, status=status.HTTP_200_OK)
