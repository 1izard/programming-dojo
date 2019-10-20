from django.shortcuts import render, redirect
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
    context = {}
    return render(request, 'izanamijinja/zenshin.html', context)


def shiren(request):
    context = {}
    return render(request, 'izanamijinja/shiren.html', context)


def zanshin(request):
    context = {}
    return render(request, 'izanamijinja/zanshin.html', context)

