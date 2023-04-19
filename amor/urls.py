from django.urls import path

from .views import poema, poema_detail

app_name = 'amor'
urlpatterns = [
    path('<int:poema_id>', poema_detail, name='poema_detail'),
    path('', poema, name='poema'),
]