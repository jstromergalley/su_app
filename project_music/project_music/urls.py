"""project_music URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView
from music import views as music_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', music_views.signup, name='signup'),
    path('admin/', admin.site.urls),
    path('admin/songs/', music_views.song_list_view_admin, name='admin_songs'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('songs/', music_views.song_list_view, name='songs'),

    path('songs_by_auth/', music_views.songs_by_auth, name='songs_by_auth'),

    path('library/', music_views.song_library, name='song_library'),
    path('library/upload/', music_views.song_new, name='song_new'),
    path('library/update/<int:song_id>', music_views.song_update, name='song_new'),
    path('library/delete/<int:song_id>', music_views.song_delete, name='song_new')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
