from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    STATUS_CHOICES = (
        ('available', 'Доступен'),
        ('sold', 'Продан'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='available')
    purchase_date = models.DateTimeField(null=True, blank=True)  # Это поле может быть пустым, если товар не продан

    def __str__(self):
        return self.name
