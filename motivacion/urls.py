from django.urls import path
from .views import poemo, poemo_detail

app_name = 'motivacion'
urlpatterns = [
    path('', poemo, name='poemo'),
    path('<int:poemo_id>', poemo_detail, name='poemo_detail')
]
