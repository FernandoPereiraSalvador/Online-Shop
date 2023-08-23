from django.shortcuts import render, HttpResponse


# Create your views here.

def home(rquest):
    return HttpResponse("Inicio")


def servicios(rquest):
    return HttpResponse("Servicios")


def tienda(rquest):
    return HttpResponse("Tienda")


def blog(rquest):
    return HttpResponse("Blog")


def contacto(rquest):
    return HttpResponse("Contacto")
