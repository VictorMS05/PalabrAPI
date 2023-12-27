from django.urls import path
from .views import PostPalabraView, GetPutPalabraView

urlpatterns = [
    path('palabra/', PostPalabraView.as_view(), name='post_palabra'),
    path('palabra/<int:clave>', GetPutPalabraView.as_view(), name='get_put_palabra'),
]
