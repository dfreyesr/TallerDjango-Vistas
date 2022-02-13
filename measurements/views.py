from django.shortcuts import render

# Create your views here.
from .logic import logic_measurements as ml
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

def measurements_view(request):
    if request.method == 'GET':
        measurements = ml.get_measurements()
        measurements_dto = serializers.serialize('json', measurements)
        return HttpResponse(measurements_dto, 'application/json')

def measurement_view(request, pk):
    if request.method == 'GET':
        measurement_dto = ml.get_measurement(pk)
        measurement = serializers.serialize('json', [measurement_dto, ])
        return HttpResponse(measurement, 'application/json')
