from django.db import models

class Registration(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=256)
    

    def __str__(self):
        return f"{self.id}. {self.name}"

class Student(models.Model):
    choises = (
        ("Kompyuter_inginiringi", "Kompyuter_inginiringi"),
        ("Axborot_texnologiyalar", "Axborot_texnologiyalar")
    )
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    faculty = models.CharField(choices=choises)
    group_name = models.CharField(max_length=64)
    theme_name = models.TextField()
    years = models.CharField(max_length=32)
    files = models.FileField(upload_to='student_files/')

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.theme_name}  - {self.years}"




