from django.urls import path
from .views import StoriesView, CardListView

urlpatterns = [
    path("stories", StoriesView.as_view(), name="stories"),
    path('card/type/', CardListView.as_view(), name='card-type-list'),
]