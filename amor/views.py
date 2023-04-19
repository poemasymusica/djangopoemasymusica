from django.shortcuts import render, get_object_or_404
from . models import Poema

def poema(request):
    poema_list = Poema.objects.all()

    return render(request, "amor.html", {
        "poema_list": poema_list
    })



def poema_detail(request, poema_id):
    poema = get_object_or_404(Poema, pk=poema_id)
    return render(request, 'poema_detail.html', {
        'poema': poema
    })

