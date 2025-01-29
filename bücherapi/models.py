from django.db import models

# Create your models here.

class Autor(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.DateField()
    nationality = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    

class Buch(models.Model):
    titel = models.CharField(max_length=100)
    autors = models.ManyToManyField(Autor, related_name='bücher') # hier ist beispiel für many to many in diesem fall braucht man kein on_delete
    isbn = models.CharField(max_length=13)
    erscheinungsdatum = models.DateField()

    def __str__(self):
        return self.title
    

