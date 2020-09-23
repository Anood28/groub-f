from django.db import models

# Create your models here.

class Project(models.Model):
    ProdName = models.CharField(max_length=50)
    ProdDesc = models.TextField(max_length=1000)
    ProdPrice = models.DecimalField(max_digits=5, decimal_places=2)
    ProdCost = models.DecimalField(max_digits=5, decimal_places=2)
    ProdCreated = models.DateTimeField(auto_now=False)
    ProdImage = models.ImageField(upload_to='project/', blank=True, null=True)
