from datetime import date
from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(
        verbose_name="Título",
        max_length=100, 
        null=False, 
        blank=False
    )
    created_at = models.DateField(
        auto_now_add=True, 
        null=False, 
        blank=False
    )
    deadline = models.DateField(
        verbose_name="Data de entregas",
        null=False, 
        blank=False
    )
    finished_at = models.DateField(
        null=True
    )

    """ Essa classe vai ordernar nossa consulta com base de onde 
    queremos que ele se guie, e nesse caso a ordenação vai começar
    na coluna 'deadline' """
    class Meta:
        # Ordenação do menor para o maior
        ordering = ["deadline"]
        
        # Ordenação do mior para o menor
        # ordering = ["-deadline"]
        
    """
        Vamos colocar a regra da aplicação que 
        diz que ela esta completa aqui diretamente.
        E ela vai ser usada dentro de todo->views.py
    """
    def mark_has_complete(self):
        if not self.finished_at:
            self.finished_at = date.today()
            self.save()
    

# Com DateTime:
""" class Todo(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(
        auto_now_add=True, null=False, blank=False)
    deadline = models.DateTimeField(null=False, blank=False)
    finished_at = models.DateTimeField(null=True)
 """
