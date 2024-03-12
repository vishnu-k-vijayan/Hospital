from django.db import models

# Create your models here.
class Doctor_table(models.Model):
    image=models.ImageField(upload_to='pic')
    name=models.CharField(max_length=50)
    department=models.CharField(max_length=50)
    qualification=models.CharField(max_length=50)
    discription=models.CharField(max_length=150)
    ph_no=models.IntegerField(max_length=50)
    

    def __str__ (self):
        return self.name

class Department_table(models.Model):
    d_name=models.CharField(max_length=50)
    discription=models.CharField(max_length=5000)
    image=models.ImageField(upload_to='pic')

    def __str__ (self):
        return self.d_name        