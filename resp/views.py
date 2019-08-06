from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def html(request):
    response = HttpResponse()
    response.write("<h2><center>Welcome To Django!</center></h2>")
    return response

def json(request):
    return JsonResponse({'foo': 'bar'})