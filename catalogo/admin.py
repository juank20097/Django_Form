from django.contrib import admin
from .models import Analista_Calidad,Unidad_Requirente,Esquema,Objetos_BDD,Componente_Objeto, Aplicativo_Afectado, Aplicativo_Desplegado, Desarrolladores,Lideres, Negocios, QAStandBy, Responsable_Branch, Responsable_Ejecucion,Responsable_Tag, Testers
# Register your models here.
admin.site.register(Analista_Calidad),
admin.site.register(Aplicativo_Afectado),
admin.site.register(Aplicativo_Desplegado),
admin.site.register(Desarrolladores),
admin.site.register(Lideres),
admin.site.register(Negocios),
admin.site.register(QAStandBy),
admin.site.register(Responsable_Branch),
admin.site.register(Responsable_Ejecucion),
admin.site.register(Responsable_Tag),
admin.site.register(Testers),
admin.site.register(Unidad_Requirente),
admin.site.register(Esquema),
admin.site.register(Objetos_BDD),
admin.site.register(Componente_Objeto),
