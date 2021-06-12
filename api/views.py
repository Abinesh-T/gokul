from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework import permissions


def index(request):
    data = Data.objects.all()
    template = loader.get_template('index.html')
    context = {
        'latest_question_list': data,
    }
    return HttpResponse(template.render(context, request))


class DataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Data.objects.all().order_by('-id')[:10]
    serializer_class = DataSerializer
