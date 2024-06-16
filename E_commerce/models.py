from django.db import models


# Create your models here.
class Product(models.Model):
    name =models.CharField(max_length=50)
    description =models.TextField(max_length=300)
    price =models.DecimalField(max_digits=9, decimal_places=2)
    image= models.ImageField(upload_to='products/')
    Availability = models.BooleanField(default=True)

def __str__(self):
    return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null= True)
    address = models.TextField(blank= True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email}"
    


