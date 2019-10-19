from django.shortcuts import render
from django.views import generic

from .models import *


def index(request):
    context = {}
    return render(request, 'mugenjigoku/index.html', context)


class ShingiView(generic.CreateView):
    model = Waza 
    template_name = 'mugenjigoku/shingi_form.html'
    fields = ('wazamoku', 'toi', 'kai1', 'kai2', 'kai3')

    def form_valid(self, form):
        return super().form_valid(form)


def zenshin(request):
    context = {}
    return render(request, 'mugenjigoku/zenshin.html', context)


def shiren(request):
    context = {}
    return render(request, 'mugenjigoku/shiren.html', context)


def zanshin(request):
    context = {}
    return render(request, 'mugenjigoku/zanshin.html', context)

