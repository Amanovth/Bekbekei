from os.path import splitext
from rest_framework import serializers
from .models import Stories, StoryVideos
from .services import video_extensions


class StoryVideosSerializers(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()
    duration = serializers.SerializerMethodField()

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


class StoriesSerializers(serializers.ModelSerializer):
    stories = StoryVideosSerializers(many=True)

    class Meta:
        model = Stories
        fields = ["id", "img", "created_at", "stories"]
