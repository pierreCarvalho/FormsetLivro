from datetime import datetime
import hashlib
import random

from django.db import models
from django.urls import reverse

class Livro(models.Model): 
    nome = models.CharField(('Nome'), max_length=50, blank = True, null = True)
    autor = models.CharField(('Autor'),max_length = 50, blank = True, null = True )
    autor_email = models.EmailField(('E-mail do autor'), blank=True, null=True)
    editora = models.CharField(('Editora'), max_length=50, blank = True, null = True)
    ano = models.IntegerField(('Ano'), blank = True, null = True)
    slug = models.SlugField(max_length=100, blank=True, unique=True, null=True)

    @property
    def get_list_url(self):
        return reverse('livro:update',kwargs={'slug':self.slug})

    def gerar_hash(self):
        return hashlib.sha256(str(random.getrandbits(256)).encode('utf-8')).hexdigest()
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = self.gerar_hash()
        super(Livro, self).save(*args, **kwargs)

    def __str__(self):
        return self.nome

class Dependente(models.Model):
    livro = models.ForeignKey('Livro',on_delete=models.PROTECT)
    nome_autor = models.CharField(('Nome do autor'), max_length=40)
    email = models.EmailField(('E-mail'), blank=True, null=True)
    slug = models.SlugField(max_length=100, blank=True, unique=True, null=True)

    @property
    def get_list_url(self):
        return reverse('livro:update',kwargs={'slug':self.slug})
    
    def gerar_hash(self):
        return hashlib.sha256(str(random.getrandbits(256)).encode('utf-8')).hexdigest()
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = self.gerar_hash()
        super(Dependente, self).save(*args, **kwargs)
