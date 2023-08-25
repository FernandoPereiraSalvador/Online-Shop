from django.shortcuts import render

# Create your views here.
from servicios.models import Servicio


def servicios(request):

    servicios = Servicio.objects.all()
    return render(request,"servicios/servicios.html",{"servicios":servicios})
