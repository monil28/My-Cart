from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=30)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.product_name