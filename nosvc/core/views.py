# coding: utf-8
from django.shortcuts import render


def home(request):
    return render(request, 'core/base.html')


def meeting_detail(request, slug):
    return render(request, 'core/meeting_detail.html')
