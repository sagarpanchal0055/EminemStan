from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)
from .forms import AlbumModelForm, KamikazeModelForm, RevivalModelForm
from .models import Album, Kamikaze, Revival

# Create your views here.

# THIS IS FOR ALBUM MTBMB 

class AlbumCreateView(CreateView):
    template_name = 'album_create.html'
    form_class = AlbumModelForm
    queryset = Album.objects.all() 

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)



class AlbumListView(ListView):
    template_name = 'album_list.html'
    queryset = Album.objects.all() 


class AlbumDetailView(DetailView):
    template_name = 'album_detail.html'
    queryset = Album.objects.all() 

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Album, id = id_)


class AlbumUpdateView(UpdateView):
    template_name = 'album_create.html'
    form_class = AlbumModelForm
    queryset = Album.objects.all() 

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Album, id = id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class AlbumDeleteView(DeleteView):
    template_name = 'album_delete.html'
    queryset = Album.objects.all() 

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Album, id = id_)

    def get_success_url(self):
        return reverse('albums:album-list')


# THIS IS FOR ALBUM KAMIKAZE 

class KamikazeCreateView(CreateView):
    template_name = 'kamikaze_create.html'
    form_class = KamikazeModelForm
    queryset = Kamikaze.objects.all() 

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)



class KamikazeListView(ListView):
    template_name = 'kamikaze_list.html'
    queryset = Kamikaze.objects.all() 

    

class KamikazeDetailView(DetailView):
    template_name = 'kamikaze_detail.html'
    queryset = Kamikaze.objects.all() 

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Kamikaze, id = id_)


class KamikazeUpdateView(UpdateView):
    template_name = 'kamikaze_create.html'
    form_class = KamikazeModelForm
    queryset = Kamikaze.objects.all() 

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Kamikaze, id = id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class KamikazeDeleteView(DeleteView):
    template_name = 'kamikaze_delete.html'
    queryset = Kamikaze.objects.all() 

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Kamikaze, id = id_)

    def get_success_url(self):
        return reverse('albums:kamikaze-list')


# THIS IS FOR ALBUM KAMIKAZE 

class RevivalCreateView(CreateView):
    template_name = 'revival_create.html'
    form_class = RevivalModelForm
    queryset = Revival.objects.all() 

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)



class RevivalListView(ListView):
    template_name = 'revival_list.html'
    queryset = Revival.objects.all() 


class RevivalDetailView(DetailView):
    template_name = 'revival_detail.html'
    queryset = Revival.objects.all() 

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Revival, id = id_)


class RevivalUpdateView(UpdateView):
    template_name = 'revival_create.html'
    form_class = RevivalModelForm
    queryset = Revival.objects.all() 

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Revival, id = id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class RevivalDeleteView(DeleteView):
    template_name = 'revival_delete.html'
    queryset = Revival.objects.all() 

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Revival, id = id_)

    def get_success_url(self):
        return reverse('albums:revival-list')