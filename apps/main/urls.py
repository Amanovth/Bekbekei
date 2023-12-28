from django.urls import path
from .views import StoriesView, CardListOneView, CardListTwoView, AllCardView, CardDetailView, VersionsView, NotificationsListView, NotificationsDetailView

urlpatterns = [
    path("stories", StoriesView.as_view(), name="stories"),
    path('card/type/one', CardListOneView.as_view(), name='card-type-list1'),
    path('card/type/two', CardListTwoView.as_view(), name='card-type-list2'),
    path('card/all/', AllCardView.as_view(), name='card-list'),
    path('card/<int:pk>', CardDetailView.as_view(), name='card-detail'),
    path("versions", VersionsView.as_view(), name="versions"),
    path("notifications/", NotificationsListView.as_view(), name='notifications-list'),
    path("notifications/<int:pk>", NotificationsDetailView.as_view(), name='notification-detail'),
]