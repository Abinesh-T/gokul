from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework import permissions


def index(request):
    data = Data.objects.all()
    a = 1
    b = data.count()
    c = b-20
    for d in data:
        if c < 0:
            pass
        if c > 0:
            if a < c:
                d.delete()
        a = a+1

    template = loader.get_template('index.html')
    context = {
        'latest_question_list': data,
    }
    return HttpResponse(template.render(context, request))


class DataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Data.objects.all()
    serializer_class = DataSerializer
