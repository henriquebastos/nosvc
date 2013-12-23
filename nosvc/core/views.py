# coding: utf-8
from django.shortcuts import render
from django.views.generic import CreateView
from nosvc.core.forms import MeetingForm
from nosvc.core.models import Meeting


def home(request):
    return render(request, 'core/base.html')


def meeting_detail(request, slug):
    return render(request, 'core/meeting_detail.html')


class MeetingCreateView(CreateView):
    model = Meeting
    form_class = MeetingForm
