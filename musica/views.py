from django.shortcuts import render
from .models import Music


def music(request):
    music_list = Music.objects.all()

    return render(request, "music.html", {
        "music_list": music_list
    })