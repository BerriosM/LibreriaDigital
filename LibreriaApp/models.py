from django.db import models
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
# ...existing code...


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    email = models.EmailField(unique=True)

    class Meta:
        db_table = 'Usuario'

    def __str__(self):
        return self.nombre

class Autores(models.Model):
    id_autores = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    nacionalidad = models.CharField(max_length=100, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'Autores'

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    id_libro = models.AutoField(primary_key=True)
    id_autor = models.ForeignKey(Autores, on_delete=models.CASCADE, db_column='id_autor', related_name='libros')
    titulo = models.CharField(max_length=300)
    genero = models.CharField(max_length=100, blank=True)
    fecha_publicacion = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'Libro'

    def __str__(self):
        return self.titulo

class Resena(models.Model):
    id_resena = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='id_usuario', related_name='resenas')
    id_libro = models.ForeignKey(Libro, on_delete=models.CASCADE, db_column='id_libro', related_name='resenas')
    puntaje = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comentario = models.TextField(blank=True)
    fecha = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Resena'

    def __str__(self):
        return f'{self.id_usuario} - {self.id_libro} ({self.puntaje})'
# ...existing code...