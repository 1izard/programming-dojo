from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse
from pprint import pprint
import json
import random

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
            if '-1' in checked_ryugi_lst:
                Ryugi.objects.all().delete()
            else:
                for checked_ryugi in checked_ryugi_lst:
                    Ryugi.objects.filter(na=checked_ryugi).delete()

    context = {
        'ryugi_lst': Ryugi.objects.all(),
        'kata_lst': Kata.objects.all(),
    }
    return render(request, 'izanamijinja/index.html', context)


def filtered_index(request, ryugi_id):
    context = {
        'ryugi_lst': Ryugi.objects.all(),
        'kata_lst': Ryugi.objects.get(pk=ryugi_id).katas.all()
    }
    return render(request, 'izanamijinja/index.html', context)

class SeikeiView(generic.CreateView):
    model = Kata
    template_name = 'izanamijinja/seikei_form.html'
    fields = ('ryugi', 'kataki', 'waza1', 'waza2', 'waza3')

    def form_valid(self, form):
        return super().form_valid(form)


def muyou(request, kata_id):
    kata = Kata.objects.get(pk=kata_id)
    kata.delete()
    return redirect('izanamijinja:index')


class KataAratameView(generic.UpdateView):
    model = Kata 
    pk_url_kwarg = 'kata_id'
    template_name = 'izanamijinja/seikei_form.html'
    fields = ('ryugi', 'kataki', 'waza1', 'waza2', 'waza3')


def zenshin(request):
    context = {
        'ryugi_lst': Ryugi.objects.all()
    }
    return render(request, 'izanamijinja/zenshin.html', context)


def shiren(request):
    print('#' * 30)

    ryugi_id = int(request.POST.get('ryugi_id'))
    tekikazu = int(request.POST.get('tekikazu'))
    
    print('ryugi_id:', ryugi_id)
    print('tekikazu:', tekikazu)

    if ryugi_id == -1:
        tekishu = list(Kata.objects.all())
    else:
        tekishu = list(Ryugi.objects.get(pk=ryugi_id).katas.all())
    random.shuffle(tekishu)
    tekishu = tekishu[:min(len(tekishu), tekikazu)]

    print('tekishu', tekishu)
    print('#' * 30)

    context = {
        'shiren_dct': {
            'tekishu': [{
                'ryugi_id': kata.ryugi.id,
                'ryugi_na': kata.ryugi.na,
                'kata_id': kata.id,
                'kataki': kata.kataki,
                'waza1': kata.waza1,
                'waza2': kata.waza2,
                'waza3': kata.waza3,
                'rendo': kata.rendo,
                'migaki': 0,
                'shippai_lst': [],
            } for kata in tekishu]
        }
    }
    return render(request, 'izanamijinja/shiren.html', context)


def zanshin(request):
    print('### izanamijinja.views.zanshin ###')
    shiren_dct = json.loads(request.body)
    pprint(shiren_dct)
    for kata in shiren_dct['tekishu']:
        Kata.objects.filter(pk=kata['kata_id']).update(rendo=kata['rendo'])
    print('######')
    return HttpResponse('success from izanamijinja.views.zanshin')

