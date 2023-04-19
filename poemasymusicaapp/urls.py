from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import Settings 

from amor import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.poema, name='poema'),
    path('amor/', include('amor.urls')),
    path('motivacion/', include('motivacion.urls')),
    path('musica/', include('musica.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
