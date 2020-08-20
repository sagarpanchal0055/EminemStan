from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)
from .forms import LyricsModelForm
from .models import Lyrics

# Create your views here.

class LyricsCreateView(CreateView):
    template_name = 'Lyrics_create.html'
    form_class = LyricsModelForm
    queryset = Lyrics.objects.all() 

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)



class LyricsListView(ListView):
    template_name = 'lyrics_list.html'
    queryset = Lyrics.objects.all() 


class LyricsDetailView(DetailView):
    template_name = 'lyrics_detail.html'
    queryset = Lyrics.objects.all() 

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Lyrics, id = id_)


class LyricsUpdateView(UpdateView):
    template_name = 'lyrics_create.html'
    form_class = LyricsModelForm
    queryset = Lyrics.objects.all() 

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Lyrics, id = id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)