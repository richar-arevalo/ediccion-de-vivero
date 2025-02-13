from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Producto(models.Model):
    name = models.CharField("Nombre", max_length=50)
    description = models.TextField('Descripcion', blank=True)
    price = models.DecimalField("Precio", max_digits=10, decimal_places=2)
    stock = models.PositiveBigIntegerField("Stock")
    image = models.ImageField('Imagen', upload_to="productos/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Compra(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='compras')
    product = models.ForeignKey(Producto, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"