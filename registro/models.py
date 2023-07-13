from django.db import models
from catalogo.models import Testers,Unidad_Requirente,Esquema,Objetos_BDD,Componente_Objeto,Analista_Calidad,Aplicativo_Afectado,Aplicativo_Desplegado,Desarrolladores,Lideres,Negocios,QAStandBy,Responsable_Branch,Responsable_Ejecucion,Responsable_Tag

# Create your models here.
class Comite(models.Model):
    tipo_paso_produccion = [
    ('planificado', 'Planificado'),
    ('emergente', 'Emergente'),
]
    tipo_estado_flujo = [
    ('Desarrollo', 'Desarrollo'),
    ('QA', 'QA'),
    ('Negocio', 'Negocio'),
]
    tipo_despliegue = [
    ('APP', 'APP'),
    ('APP-BDD', 'APP-BDD'),
    ('BDD', 'BDD'),
]
    tipo_script = [
    ('DML+DDL', 'DML+DDL'),
    ('DML', 'DML'),
    ('DDL', 'DDL'),
    ('DCL', 'DCL'),
]
    tipo_bdd = [
    ('Oracle', 'Oracle'),
    ('Postgresql', 'Postgresql'),
    ('DB2', 'DB2'),
]
    tipo_estado = [
    ('No aplicado en producción', 'No aplicado en producción'),
    ('Por aplicar en producción', 'Por aplicar en producción'),
    ('Aplicado en producción', 'Aplicado en producción'),
    ('Reversado', 'Reversado'),
]

    id_comite = models.AutoField(primary_key=True)
    fecha_del_requerimiento = models.DateField(null=True)
    tipo_paso_produccion = models.CharField(max_length=255, choices=tipo_paso_produccion, null=True)
    numero_requerimiento = models.CharField(max_length=255, null=True)
    estado_flujo_req = models.CharField(max_length=255, choices=tipo_estado_flujo, null=True)
    breve_descripcion_req = models.CharField(max_length=255, null=True)
    tipo_despliegue = models.CharField(max_length=255, choices=tipo_despliegue, null=True)
    tipo_script = models.CharField(max_length=255, choices=tipo_script, null=True)
    tipo_bdd = models.CharField(max_length=255, choices=tipo_bdd, null=True)
    formulario_menus = models.BooleanField(default=False)
    lider = models.ForeignKey(Lideres, on_delete=models.CASCADE,null=True)
    desarrollador = models.ForeignKey(Desarrolladores, on_delete=models.CASCADE,null=True)
    negocio = models.ForeignKey(Negocios, on_delete=models.CASCADE,null=True)
    fecha_asignacion_calidad = models.DateField(null=True)
    dias_planificados_pruebas = models.IntegerField(null=True)
    tester = models.ForeignKey(Testers, on_delete=models.CASCADE,null=True)
    qa_stand_by = models.ForeignKey(QAStandBy, on_delete=models.CASCADE, null=True)
    aplicativos_desplegados = models.ForeignKey(Aplicativo_Desplegado, on_delete=models.CASCADE, null=True)
    aplicativos_afectados = models.ForeignKey(Aplicativo_Afectado, on_delete=models.CASCADE, null=True)
    estado = models.CharField(max_length=255, choices=tipo_estado, null=True)
    fecha_hora = models.DateField(null=True)
    responsable_ejecucion = models.ForeignKey(Responsable_Ejecucion, on_delete=models.CASCADE, null=True)
    fecha_ejecucion = models.DateField(null=True)
    tiempo_ejecucion = models.FloatField(null=True)
    fecha_reversa = models.DateField(null=True)
    observaciones_paso_produccion = models.CharField(max_length=255, null=True)
    fecha_comite = models.DateField(null=True)
    afectacion_objetos_core = models.BooleanField(default=False)
    fecha_asignacion_seguridad = models.DateField(null=True)
    fecha_real_asignacion_calidad = models.DateField(null=True)
    fecha_real_asignacion_seguridad = models.DateField(null=True)
    fecha_real_asignacion_plataforma = models.DateField(null=True)
    observacion_calidad = models.CharField(max_length=255, null=True)
    responsable_creacion_branch = models.ForeignKey(Responsable_Branch, on_delete=models.CASCADE, null=True)
    responsable_creacion_tag = models.ForeignKey(Responsable_Tag, on_delete=models.CASCADE, null=True)
    fecha_creacion_tag = models.DateField(null=True)
    fecha_creacion_branch = models.DateField(null=True)
    fecha_ejecucion_pruebas = models.DateField(null=True)
    analista_calidad_ejecucion_pruebas = models.ForeignKey(Analista_Calidad, on_delete=models.CASCADE, null=True)
    autorizador_paso_produccion = models.BooleanField(default=False)

    def __str__(self):
        return self.fecha_del_requerimiento.strftime("%Y-%m-%d %H:%M:%S")

class Objeto(models.Model):
    tipo_version = [
    ('PAS-GUI-018 1.0', 'PAS-GUI-018 1.0'),
    ('PAS-GUI-018 2.0', 'PAS-GUI-018 2.0'),
]
    tipo_bdd = [
    ('Oracle', 'Oracle'),
    ('Postgresql', 'Postgresql'),
    ('DB2', 'DB2'),
]
    tipo_accion = [
    ('Creación', 'Creación'),
    ('Modificación', 'Modificación'),
]
    tipo_cambio = [
    ('Reunión', 'Reunión'),
    ('Lineamiento Arquitectura', 'Lineamiento Arquitectura'),
]
    tipo_flujo = [
    ('Preproducción', 'Preproducción'),
    ('Producción', 'Producción'),
]
    id_objeto = models.AutoField(primary_key=True)
    version_documento = models.CharField(max_length=255,choices=tipo_version,null=True)
    requerimiento = models.CharField(max_length=255,null=True)
    unidad_requirente = models.ForeignKey(Unidad_Requirente, on_delete=models.CASCADE,null=True)
    base_de_datos = models.CharField(max_length=100,choices=tipo_bdd,null=True)
    tipo_de_objeto = models.CharField(max_length=255,null=True)
    esquema = models.ForeignKey(Esquema, on_delete=models.CASCADE,null=True)
    tipo_accion = models.CharField(max_length=255,choices=tipo_accion,null=True)
    objetos_de_base_de_datos = models.ForeignKey(Objetos_BDD, on_delete=models.CASCADE,null=True)
    componente = models.ForeignKey(Componente_Objeto, on_delete=models.CASCADE,null=True)
    fecha = models.DateField(null=True)
    tipo_cambio = models.CharField(max_length=255,choices=tipo_cambio,null=True)
    usuario_gitlab = models.CharField(max_length=255,null=True)
    estado_flujo_objeto = models.CharField(max_length=255,choices=tipo_flujo,null=True)
    fecha_versionamiento = models.DateField(null=True)
    numero_iteracion = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    observacion = models.TextField(null=True)
    fecha_inventario = models.DateField(null=True)

    def __str__(self):
        return '%s %s'  % (self.requerimiento,self.esquema) 
