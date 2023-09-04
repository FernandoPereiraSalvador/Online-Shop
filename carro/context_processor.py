def importe_total_carro(request):
    total = 0
    if request.user.is_authenticated:
        for key, value in request.session["carro"].items():
            total += float(value["precio"])

    else:
        total = "Necesitas iniciar sesión"

    return {"importe_total_carro": total}
