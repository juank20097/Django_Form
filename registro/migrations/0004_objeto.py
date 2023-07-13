# Generated by Django 4.2.3 on 2023-07-11 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_componente_objeto_esquema_objetos_bdd_and_more'),
        ('registro', '0003_alter_comite_analista_calidad_ejecucion_pruebas_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Objeto',
            fields=[
                ('id_objeto', models.AutoField(primary_key=True, serialize=False)),
                ('version_documento', models.CharField(choices=[('PAS-GUI-018 1.0', 'PAS-GUI-018 1.0'), ('PAS-GUI-018 2.0', 'PAS-GUI-018 2.0')], max_length=255, null=True)),
                ('requerimiento', models.CharField(max_length=255, null=True)),
                ('base_de_datos', models.CharField(choices=[('Oracle', 'Oracle'), ('Postgresql', 'Postgresql'), ('DB2', 'DB2')], max_length=255, null=True)),
                ('tipo_de_objeto', models.CharField(max_length=255, null=True)),
                ('tipo_accion', models.CharField(choices=[('Creación', 'Creación'), ('Modificación', 'Modificación')], max_length=255, null=True)),
                ('fecha', models.DateField(null=True)),
                ('tipo_cambio', models.CharField(choices=[('Reunión', 'Reunión'), ('Lineamiento Arquitectura', 'Lineamiento Arquitectura')], max_length=255, null=True)),
                ('usuario_gitlab', models.CharField(max_length=255, null=True)),
                ('estado_flujo_objeto', models.CharField(choices=[('Preproducción', 'Preproducción'), ('Producción', 'Producción')], max_length=255, null=True)),
                ('fecha_versionamiento', models.DateField(null=True)),
                ('numero_iteracion', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('observacion', models.TextField(null=True)),
                ('fecha_inventario', models.DateField(null=True)),
                ('componente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.componente_objeto')),
                ('esquema', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.esquema')),
                ('objetos_de_base_de_datos', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.objetos_bdd')),
                ('unidad_requirente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.unidad_requirente')),
            ],
        ),
    ]