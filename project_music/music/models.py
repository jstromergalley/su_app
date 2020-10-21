from django.db import models
from django.conf import settings

# Create your models here.
class Song(models.Model):

    class Meta:
        unique_together = [('username', 'artist', 'name')]

    username = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        to_field="username",
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=100, verbose_name="Song's Title")
    artist = models.CharField(max_length=100, verbose_name="Artist's Name")

    def __str__(self):
        return str(self.username) + " : " + str(self.artist) + " : " + str(self.name)
