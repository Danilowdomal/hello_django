from django.shortcuts import render, HttpResponse


# Create your views here.

def hello(request, nome, idade):
    return HttpResponse("<h1>Olá {}, você tem {} anos</h1>".format(nome, idade))


def soma(request, a, b):
    return HttpResponse(a + b)


def sub(request, a, b):
    return HttpResponse(a - b)


def mul(request, a, b):
    return HttpResponse(a * b)


def div(request, a , b):
    return HttpResponse(a / b)
