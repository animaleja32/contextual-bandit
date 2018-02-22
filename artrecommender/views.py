# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'artrecommender/index.html', context)

def joy(request):
    return render(request, 'artrecommender/joy.html')

def black_panther(request):
    return render(request, 'artrecommender/black_panther.html')

def pj_masks(request):
    return render(request, 'artrecommender/pj_masks.html')