import django_tables2 as tables

from .models import Song

class SongTable(tables.Table):
    class Meta:
        model = Song
        template_name = "django_tables2/bootstrap4.html"
        fields = ("artist", "name")
