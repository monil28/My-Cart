from django.db import models


# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=30)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=500)
    pub_date = models.DateField()
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.product_name
    

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name
