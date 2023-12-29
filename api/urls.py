from django.urls import path
from .views import GetPalabraView, PostPalabraView, PutPalabraView

urlpatterns = [
    path('palabra/<int:clave>', GetPalabraView.as_view(), name='get_palabra'),
    path('palabra/', PostPalabraView.as_view(), name='post_palabra'), # El endpoint para agregar una palabra está incompleto, solo el administrador tiene acceso al endpoint correcto
    path('palabra/<int:clave>', PutPalabraView.as_view(), name='put_palabra'), # El endpoint para modificar una palabra está incompleto, solo el administrador tiene acceso al endpoint correcto
]
