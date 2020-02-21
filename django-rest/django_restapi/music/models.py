from django.db import models

# Create your models here.
#primary key or id
class Album(models.Model):
    artist = models.CharField(max_length=256)
    album_title = models.CharField(max_length=256)
    genre = models.CharField(max_length=256)
    album_logo = models.CharField(max_length=1024)
    def __str__(self):
        return self.artist + ", " + self.album_title + ", " + self.genre
class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=4)
    song_title = models.CharField(max_length=256)
    def __str__(self):
        return self.file_type + ", " + self.song_title
