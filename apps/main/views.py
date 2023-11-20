from rest_framework.generics import ListAPIView
from rest_framework import generics
from .models import Stories, Cards
from .serializers import StoriesSerializers, CardSerializers


class StoriesView(ListAPIView):
    queryset = Stories.objects.all()
    serializer_class = StoriesSerializers


class CardListView(generics.ListAPIView):
    queryset = Cards.objects.all()
    serializer_class = CardSerializers


class CardDetailView(generics.RetrieveAPIView):
    queryset = Cards.objects.all()
    serializer_class = CardSerializers