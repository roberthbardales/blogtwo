from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=200,unique=True, verbose_name='Nombre')
    active = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')
    updated= models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificacion')
    class Meta:

        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering=['name']

    def __str__(self):
        return self.name



class Tag(models.Model):

    name = models.CharField(max_length=200,unique=True, verbose_name='Nombre')
    active = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificacion')
    class Meta:

        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'
        ordering=['name']

    def __str__(self):
        return self.name

class Posts(models.Model):

    title = models.CharField(max_length=250, verbose_name='Titulo')
    excerpt = models.TextField(verbose_name='Bajada')
    content = models.TextField(verbose_name='Contenido')
    image = models.ImageField(upload_to='posts', null=True, blank=True, verbose_name='Imagen')
    published = models.BooleanField(default=False, verbose_name='Publicado')

    #relacionados
    category = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name='Categoria')
    author = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='Autor')
    tags = models.ManyToManyField(Tag,verbose_name='Etiquetas')

    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')
    update = models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificacion')

    class Meta:

        verbose_name = 'Posts'
        verbose_name_plural = 'Postss'
        ordering=['title']

    def __str__(self):
        return self.title


class About(models.Model):

    descripcion = models.CharField(max_length=350, verbose_name='Descripcion')
    active = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificacion')
    class Meta:

        verbose_name = 'Acerca de'
        verbose_name_plural = 'Acerca de Nosotros'
        ordering=['-created']

    def __str__(self):
        return self.descripcion

class Link(models.Model):

    key = models.CharField(max_length=100, verbose_name='Key Link')
    name = models.CharField(max_length=100, verbose_name='Red Social')
    url = models.URLField(max_length=350,blank=True,null=True, verbose_name='Enlace' )
    icon = models.CharField(max_length=100,blank=True,null=True,     verbose_name='Icono')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificacion')
    class Meta:

        verbose_name = 'Red Social'
        verbose_name_plural = 'Redes Sociales'
        ordering=['-name']

    def __str__(self):
        return self.name








