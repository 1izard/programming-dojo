from django.shortcuts import render
from django.views import generic
from pprint import pprint
import json

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

    ryugi_lst = list(Ryugi.objects.all())
    
    ryugi_lst = [{
        'id': ryugi.id,
        'kotodute': ryugi.kotodute,
        'na': ryugi.na,
    } for ryugi in ryugi_lst]

    kata_lst = list(Kata.objects.all())
    kata_lst = [{
        'id': kata.id,
        'kataki': kata.kataki,
        'rendo': kata.rendo,
        'ryugi_id': kata.ryugi_id,
        'waza1': kata.waza1,
        'waza2': kata.waza2,
        'waza3': kata.waza3
    } for kata in kata_lst]

    context = {
        'ryugi_dct': {
            'ryugi_lst': ryugi_lst,
        },
        'katas_dct': {
            'kata_lst': kata_lst,
        },
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

