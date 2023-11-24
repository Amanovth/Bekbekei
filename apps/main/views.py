from rest_framework.generics import ListAPIView
from rest_framework import generics
from .models import Stories, Cards, Versions
from .serializers import StoriesSerializers, CardSerializers, VersionsSerializer


class StoriesView(ListAPIView):
    queryset = Stories.objects.all()
    serializer_class = StoriesSerializers


class CardListView(generics.ListAPIView):
    queryset = Cards.objects.all()
    serializer_class = CardSerializers


class CardDetailView(generics.RetrieveAPIView):
    queryset = Cards.objects.all()
    serializer_class = CardSerializers


class VersionsView(generics.RetrieveAPIView):
    serializer_class = VersionsSerializer

    def get_object(self):
        return Versions.objects.latest("date")