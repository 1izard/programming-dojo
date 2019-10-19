from django.shortcuts import render
from django.views import generic
from pprint import pprint

from .models import *
from .forms import *


def index(request):
    if request.method == 'POST':
        if request.POST.get('act') == 'soushi':
            shin_ryugi_mei = request.POST.get('shin_ryugi_mei')
            if 0 < len(shin_ryugi_mei) < 20:
                Ryugi.objects.create(na=shin_ryugi_mei, kotodute='')
        elif request.POST.get('act') == 'shitsuden':
            checked_ryugi_lst = request.POST.getlist('checked_ryugis')
            for checked_ryugi in checked_ryugi_lst:
                Ryugi.objects.filter(na=checked_ryugi).delete()

    context = {
        'ryugi_lst': Ryugi.objects.all(),
    }
    return render(request, 'izanamijinja/index.html', context)


class SeikeiView(generic.CreateView):
    model = Kata 
    template_name = 'izanamijinja/seikei_form.html'
    fields = ('ryugi', 'kataki', 'waza1', 'waza2', 'waza3')

    def form_valid(self, form):
        return super().form_valid(form)


def zenshin(request):
    context = {}
    return render(request, 'izanamijinja/zenshin.html', context)


def shiren(request):
    context = {}
    return render(request, 'izanamijinja/shiren.html', context)


def zanshin(request):
    context = {}
    return render(request, 'izanamijinja/zanshin.html', context)

