from django.shortcuts import render, get_object_or_404
from . models import Poemo

def poemo(request):
    poemo_list = Poemo.objects.all()

    return render(request, "motivacion.html", {
        "poemo_list": poemo_list
    })



def poemo_detail(request, poemo_id):
    poemo = get_object_or_404(Poemo, pk=poemo_id)
    return render(request, 'poemo_detail.html', {
        'poemo': poemo
    })
