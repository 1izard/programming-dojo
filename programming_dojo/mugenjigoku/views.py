from django.shortcuts import render
from django.views import generic

from .models import *


class IndexView(generic.ListView):
    model = Wazamoku
    template_name = 'mugenjigoku/index.html'
    context_object_name = 'wazamoku_lst'
