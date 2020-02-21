from rest_framework import serializers
from . import models

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Album
        fields = ('id', 'album_title', 'artist', 'genre', 'album_logo')


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Song
        fields = ('album','id', 'song_title', 'file_type')
