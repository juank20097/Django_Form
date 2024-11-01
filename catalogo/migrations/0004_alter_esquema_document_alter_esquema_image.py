# Generated by Django 4.2.7 on 2024-10-30 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0003_esquema_document_esquema_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='esquema',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='esquema',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
