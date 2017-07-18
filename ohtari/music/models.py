from django.db import models


class Album(models.Model):
    artist = models.CharField(max_length=50)
    album_title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.album_title + ' - ' + self.artist


class Song(models.Model):
    song_name = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete = models.CASCADE)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_name
