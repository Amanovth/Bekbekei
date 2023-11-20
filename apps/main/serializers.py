from os.path import splitext
from rest_framework import serializers
from .models import Stories, StoryVideos, Cards
from .services import video_extensions
import locale

locale.setlocale(
    category=locale.LC_ALL)


class StoryVideosSerializers(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()
    duration = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()

    class Meta:
        model = StoryVideos
        fields = [
            "type",
            "url",
            "duration",
            "created_at",
        ]

    def get_type(self, obj):
        _, file_extension = splitext(obj.url.name.lower())

        if file_extension in video_extensions:
            return "video"
        return "image"

    def get_duration(self, obj):
        return 10000

    def get_url(self, obj):
        return f"https://bekbekei.store{obj.url.url}"


class StoriesSerializers(serializers.ModelSerializer):
    stories = StoryVideosSerializers(many=True)
    img = serializers.SerializerMethodField()

    class Meta:
        model = Stories
        fields = ["id", "img", "created_at", "stories", "link"]

    def get_img(self, obj):
        return f"https://bekbekei.store{obj.img.url}"


class CardSerializers(serializers.ModelSerializer):
    datefrom = serializers.SerializerMethodField()
    dateto = serializers.SerializerMethodField()
    date = serializers.SerializerMethodField()

    class Meta:
        model = Cards
        fields = "__all__"

    def get_datefrom(self, obj):
        if obj.datefrom:
            return obj.datefrom.strftime("%d.%m")

    def get_dateto(self, obj):
        if obj.dateto:
            return obj.dateto.strftime("%d.%m")
        
    def get_date(self, obj):
        locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
        if obj.date:
            return obj.dateto.strftime("Акция действует до: %d %B %Y")


# self.date = self.dateto.strftime()