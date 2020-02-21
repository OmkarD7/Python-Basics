from rest_framework import serializers
from . import models

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Album
        fields = ('id', 'album_title')


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Song
        fields = ('id', 'song_title')
