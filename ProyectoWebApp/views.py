from django.shortcuts import render, HttpResponse

# Create your views here.
from carro.carro import Carro


def home(request):

    carro = Carro(request)

    return render(request,"home.html")

