from django.db import models

class Registration(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=256)
    

    def __str__(self):
        return f"{self.id}. {self.name}"





