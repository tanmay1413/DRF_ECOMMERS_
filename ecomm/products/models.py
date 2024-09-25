from django.db import models

# Create your models here.
class products(models.Model):
    PRODUCT_TYPE_CHOICES = [
        ('electronics', 'Electronics'),
        ('fashion', 'Fashion'),
        ('groceries', 'Groceries'),
        ('furniture', 'Furniture'),
        # Add other categories as needed
    ]
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    price = models.IntegerField()
    stock = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20 , choices=PRODUCT_TYPE_CHOICES)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to='product_images/') 
    
    def __str__(self):
        return self.name
    