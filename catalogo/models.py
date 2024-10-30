from django.db import models

## Entidades de catalogo de Comite

class Lideres(models.Model):
    id = models.AutoField(primary_key=True)
    nombres_completos = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.nombres_completos

class Desarrolladores(models.Model):
    id = models.AutoField(primary_key=True)
    nombres_completos = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.nombres_completos

class Negocios(models.Model):
    id = models.AutoField(primary_key=True)
    nombres_completos = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.nombres_completos

class Testers(models.Model):
    id = models.AutoField(primary_key=True)
    nombres_completos = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.nombres_completos

class QAStandBy(models.Model):
    id = models.AutoField(primary_key=True)
    nombres_completos = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.nombres_completos

class Aplicativo_Desplegado(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.nombre

class Aplicativo_Afectado(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.nombre

class Responsable_Ejecucion(models.Model):
    id = models.AutoField(primary_key=True)
    nombres_completos = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.nombres_completos

class Responsable_Branch(models.Model):
    id = models.AutoField(primary_key=True)
    nombres_completos = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.nombres_completos

class Responsable_Tag(models.Model):
    id = models.AutoField(primary_key=True)
    nombres_completos = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.nombres_completos

class Analista_Calidad(models.Model):
    id = models.AutoField(primary_key=True)
    nombres_completos = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.nombres_completos
    
## Entidades de catalogo de Objetos

class Unidad_Requirente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.nombre
    
class Esquema(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    document = models.FileField(upload_to='documents/', null=True,  blank=True)

    def __str__(self):
        return self.nombre
    
class Objetos_BDD(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.nombre
    
class Componente_Objeto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.nombre