from django.contrib import admin
from .models import PedidosExames, SolicitacaoExame, TiposExames

admin.site.register(TiposExames)
admin.site.register(SolicitacaoExame)
admin.site.register(PedidosExames)
