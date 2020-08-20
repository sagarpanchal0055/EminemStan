from django.urls import path
from .views import (
    LyricsListView,
    LyricsDetailView,
    LyricsCreateView,
    LyricsUpdateView
)

app_name = 'lyrics'
urlpatterns = [
    path('', LyricsListView.as_view() , name='lyrics-list'), 
    path('<str:album_id>/', LyricsDetailView.as_view() , name='lyrics-detail'), 
    path('create/', LyricsCreateView.as_view() , name='lyrics-create'), 
    path('<int:id>/update', LyricsUpdateView.as_view() , name='lyrics-update'), 
]