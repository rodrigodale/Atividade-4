from django.db import models


class Paisagens(models.Model):
  nome_da_paisagem = models.CharField(max_length=50)
  localizacao = models.CharField(max_length=50)
  clima = models.CharField(max_length=50)
  altitude = models.CharField(max_length=50) 

class Curiosidades(models.Model):
  VISITA = [("N", "Nunca"),
             ("A","As vezes"),
             ("S","Sempre")
            ]
  CATEGORIA = [("A", "AMIGOS"),
             ("D","DATE"),
             ("F","FAMILIA")
            ]

  
  nome_da_paisagem = models.CharField(max_length=50)
  frequencia =models.CharField(max_length=1, choices=VISITA)
  prioridade_de_visita = models.IntegerField()
  categoria = models.CharField(max_length=1, choices=CATEGORIA) 