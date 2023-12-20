from rest_framework.generics import ListAPIView
from rest_framework import generics
from .models import Stories, Cards, Versions, Notifications
from .serializers import (
    StoriesSerializers,
    CardSerializers,
    VersionsSerializer,
    NotificationsSerializer,
)


class StoriesView(ListAPIView):
    queryset = Stories.objects.all()
    serializer_class = StoriesSerializers


class CardListView(generics.ListAPIView):
    queryset = Cards.objects.all()
    serializer_class = CardSerializers


class CardDetailView(generics.RetrieveAPIView):
    queryset = Cards.objects.all()
    serializer_class = CardSerializers


class NotificationsListView(generics.ListAPIView):
    queryset = Notifications.objects.order_by('-id')
    serializer_class = NotificationsSerializer


class NotificationsDetailView(generics.RetrieveAPIView):
    queryset = Notifications.objects.all()
    serializer_class = NotificationsSerializer


class VersionsView(generics.RetrieveAPIView):
    serializer_class = VersionsSerializer

    def get_object(self):
        return Versions.objects.latest("date")
