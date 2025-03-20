from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    dataNascimento = models.IntegerField()
    genero = models.CharField(max_length=100)
    cpf = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    

