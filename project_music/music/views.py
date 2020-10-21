import django_tables2 as tables
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Count
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView
from django_tables2 import RequestConfig, SingleTableView

from .forms import SongCreate
from .models import Song
from .tables import SongTable

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def songs_by_auth(request):
    return HttpResponseRedirect(reverse("admin_songs")) if request.user.is_superuser or request.user.is_staff else HttpResponseRedirect(reverse("songs"))

@user_passes_test(lambda u: u.is_superuser)
def song_list_view_admin(request):
    class NameTable(tables.Table):
        class Meta:
            template_name = "django_tables2/bootstrap4.html"

        artist = tables.Column()
        name = tables.Column()
        user_count = tables.Column()

    all_songs = (
        Song
            .objects
            .values("name", "artist")
            .annotate(user_count=Count("username"))
            .order_by("-user_count")
    )
    table = NameTable(all_songs)
    RequestConfig(request).configure(table)

    class NameTable2(tables.Table):
        class Meta:
            template_name = "django_tables2/bootstrap4.html"

        artist = tables.Column()
        user_count = tables.Column()

    all_songs = (
        Song
            .objects
            .values("artist")
            .annotate(user_count=Count("username", distinct=True))
            .order_by ("-user_count")
    )
    table2 = NameTable2(all_songs)
    RequestConfig(request).configure(table2)

    return render(request, "songs_admin.html", {"table": table, "table2": table2})

@login_required
def song_list_view(request):
    table = SongTable(Song.objects.filter(username=request.user).all())
    RequestConfig(request).configure(table)
    return render(request, "songs.html", {"table": table})

@login_required
def song_library(request):
    library = Song.objects.filter(username=request.user).all()
    return render(request, 'library.html', {'library': library})

@login_required
def song_new(request):

    if not request.method == 'POST':
        form = SongCreate()
        return render(request, 'song_new.html', {'song': form})

    form = SongCreate(request.POST)

    if not form.is_valid():
        return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'song_library'}}">reload</a>""")

    new_form = form.save(commit=False)
    new_form.username = request.user

    try:
        new_form.save()
    except Exception:
        pass

    return redirect('song_library')

@login_required
def song_update(request, song_id):
    song_id = int(song_id)

    try:
        song_data = Song.objects.get(id=song_id)
    except Song.DoesNotExist:
        return redirect('song_library')

    song = SongCreate(request.POST or None, instance=song_data)

    if not song.is_valid():
        return render(request, 'song_new.html', {'song':song})

    try:
        song.save()
    except Exception:
        pass

    return redirect('song_library')

@login_required
def song_delete(request, song_id):
    song_id = int(song_id)

    try:
        song_data = Song.objects.get(id=song_id)
    except Song.DoesNotExist:
        return redirect('song_library')

    song_data.delete()
    return redirect('song_library')
