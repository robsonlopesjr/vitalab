from django.urls import path
from .views import fechar_pedido, solicitar_exames


urlpatterns = [
    path("solicitar_exames/", solicitar_exames, name="solicitar_exames"),
    path("fechar_pedido/", fechar_pedido, name="fechar_pedido"),
]
