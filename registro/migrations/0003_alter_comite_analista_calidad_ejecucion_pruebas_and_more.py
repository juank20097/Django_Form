# Generated by Django 4.2.3 on 2023-07-11 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
        ('registro', '0002_rename_registro_comite_comite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comite',
            name='analista_calidad_ejecucion_pruebas',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.analista_calidad'),
        ),
        migrations.AlterField(
            model_name='comite',
            name='aplicativos_afectados',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.aplicativo_afectado'),
        ),
        migrations.AlterField(
            model_name='comite',
            name='aplicativos_desplegados',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.aplicativo_desplegado'),
        ),
        migrations.AlterField(
            model_name='comite',
            name='desarrollador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.desarrolladores'),
        ),
        migrations.AlterField(
            model_name='comite',
            name='lider',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.lideres'),
        ),
        migrations.AlterField(
            model_name='comite',
            name='negocio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.negocios'),
        ),
        migrations.AlterField(
            model_name='comite',
            name='qa_stand_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.qastandby'),
        ),
        migrations.AlterField(
            model_name='comite',
            name='responsable_creacion_branch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.responsable_branch'),
        ),
        migrations.AlterField(
            model_name='comite',
            name='responsable_creacion_tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.responsable_tag'),
        ),
        migrations.AlterField(
            model_name='comite',
            name='responsable_ejecucion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.responsable_ejecucion'),
        ),
        migrations.AlterField(
            model_name='comite',
            name='tester',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.testers'),
        ),
    ]
