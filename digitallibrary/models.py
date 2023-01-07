from django.db import models
# Create your models here.


class Author(models.Model):
    name = models.CharField('Nombre', max_length=200, blank=False)
    nationality = models.CharField('Nacionalidad', max_length=3)

    def __str__(self):
        """Return string representation of object."""
        return self.name


class Books(models.Model):
    title = models.CharField('Título', max_length=250)
    year = models.IntegerField('Año', default=1900, )
    language = models.CharField('Idioma', max_length=2, help_text='ISO 639-1 Language code (2 chars)')
    cover_url = models.URLField('Portada', help_text='Guarda el url de una imagen', blank=True, null=True)
    price = models.DecimalField('Precio', max_digits=10, decimal_places=2, default='')
    sellable = models.BooleanField('Disponible', default=True, help_text='True disponible, False no disponible')
    copies = models.IntegerField('Copias', default=1)
    description = models.TextField('Descripción', blank=True, max_length=500)
    # blank = True hace el campo opcional, y blank = False hace el campo obligatorio
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        """Return string representation of object."""
        return self.title