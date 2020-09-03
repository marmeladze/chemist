from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)


class Drug(models.Model):
    name = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)



