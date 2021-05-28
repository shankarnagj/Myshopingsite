from django.db import models
from django.db.models.fields import EmailField
from myshop.models import Product

# Create your models here.
class Order(models.Model) :
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.EmailField()
    address = models.CharField(max_length = 250)
    landmark = models.CharField(max_length = 50)
    postal_code = models.CharField(max_length = 10)
    city = models.CharField(max_length = 20)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    paid = models.BooleanField(default = False)

    class class Meta:
       ordering = ('-created')
    
    def __str__(self) :
        return (f"Order {self.id}")
    
    def get_total_cost(self):
        return sum(item.get_cost for item in self.items.all())