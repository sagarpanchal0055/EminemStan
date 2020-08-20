from django.urls import path
from .views import (
    AlbumListView,
    AlbumDetailView,
    AlbumCreateView,
    AlbumUpdateView,
    AlbumDeleteView,

    KamikazeListView,
    KamikazeDetailView,
    KamikazeCreateView,
    KamikazeUpdateView,
    KamikazeDeleteView,

    RevivalListView,
    RevivalDetailView,
    RevivalCreateView,
    RevivalUpdateView,
    RevivalDeleteView,

)
app_name = 'albums'
urlpatterns = [
    # album MTBMB

    path('', AlbumListView.as_view() , name='album-list'), 
    path('<int:id>/', AlbumDetailView.as_view() , name='album-detail'), 
    path('create/', AlbumCreateView.as_view() , name='album-create'), 
    path('<int:id>/update', AlbumUpdateView.as_view() , name='album-update'),
    path('<int:id>/delete', AlbumDeleteView.as_view() , name='album-delete'),

    # album Kamikaze

    path('kamikaze/', KamikazeListView.as_view() , name='kamikaze-list'), 
    path('kamikaze/<int:id>/', KamikazeDetailView.as_view() , name='kamikaze-detail'), 
    path('kamikaze/create/', KamikazeCreateView.as_view() , name='kamikaze-create'), 
    path('kamikaze/<int:id>/update', KamikazeUpdateView.as_view() , name='kamikaze-update'),
    path('kamikaze/<int:id>/delete', KamikazeDeleteView.as_view() , name='kamikaze-delete'), 

    # album revival

    path('revival/', RevivalListView.as_view() , name='revival-list'), 
    path('revival/<int:id>/', RevivalDetailView.as_view() , name='revival-detail'), 
    path('revival/create/', RevivalCreateView.as_view() , name='revival-create'), 
    path('revival/<int:id>/update', RevivalUpdateView.as_view() , name='revival-update'),
    path('revival/<int:id>/delete', RevivalDeleteView.as_view() , name='revival-delete'),    
]