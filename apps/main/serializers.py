from os.path import splitext
from rest_framework import serializers
from .models import Stories, StoryVideos
from .services import video_extensions


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
        return f"http://89.223.126.144{obj.url.url}"


class StoriesSerializers(serializers.ModelSerializer):
    stories = StoryVideosSerializers(many=True)
    img = serializers.SerializerMethodField()

    class Meta:
        model = Stories
        fields = ["id", "img", "created_at", "stories"]

    def get_img(self, obj):
        return f"http://89.223.126.144{obj.img.url}"
