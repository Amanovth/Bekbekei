from django.urls import path
from .views import StoriesView, CardListView, CardDetailView, VersionsView

urlpatterns = [
    path("stories", StoriesView.as_view(), name="stories"),
    path('card/type', CardListView.as_view(), name='card-type-list'),
    path('card/<int:pk>', CardDetailView.as_view(), name='card-detail'),
    path("versions", VersionsView.as_view(), name="versions"),
]