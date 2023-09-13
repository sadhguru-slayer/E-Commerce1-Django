from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class  Brands(models.Model):
    Brand_name=models.CharField(max_length=100)

    def __str__(self):
        return self.Brand_name


class  Product_type(models.Model):
    Product_type=models.CharField(max_length=100)

    def __str__(self):
        return self.Product_type



class Categories(models.Model):
    Category=models.CharField(max_length=100)

    def __str__(self):
        return self.Category

class Price_Filter(models.Model):
    PRICE_FILTER=(
        ('100 TO 300','100 TO 300'),
        ('300 TO 500','300 TO 500'),
        ('500 TO 700','500 TO 700'),
        ('700 TO 900','700 TO 900'),
        ('900 TO 1200','900 TO 1200'),
        ('1200 TO 1500','1200 TO 1500'),
        ('1500 +','1500 +'),
        )

    price=models.CharField(choices=PRICE_FILTER,max_length=100)

    def __str__(self):
        return self.price

class Volume_Filter(models.Model):
    Volume=models.CharField(max_length=100)
    

    def __str__(self):
        return self.Volume



# Create your models here.
class Contact(models.Model):
    contact_id=models.AutoField(primary_key=True)
    email=models.EmailField()
    name=models.CharField(max_length=50)
    subject=models.CharField(max_length=500)
    message=models.TextField(max_length=1000)
    email=models.EmailField(max_length=20)


    def __str__(self):
        return self.email


class Product(models.Model):
    STOCK=('IN STOCK','IN STOCK'),('OUT OF STOCK','OUT OF STOCK'),

    product_id=models.CharField(unique=True,max_length=200,null=True,blank=True)
    name=models.CharField(max_length=255)
    product_brand = models.ForeignKey(Brands, on_delete=models.CASCADE, null=True, blank=True)
    product_categore = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, blank=True)
    Price_Filter = models.ForeignKey(Price_Filter, on_delete=models.CASCADE, null=True, blank=True)
    price=models.FloatField()
    volume=models.ForeignKey(Volume_Filter,on_delete=models.CASCADE,null=True,blank=True)
    product_desc=models.CharField(max_length=500)
    created_date = models.DateTimeField(default=timezone.now)
    image=models.ImageField(upload_to='images')
    stock=models.CharField(choices=STOCK,max_length=100)

    def __str__(self):
        template = '{0.name} {0.image} {0.price}'
        # return template.format(self)
        return template.format(self)

    def save(self, *args, **kwargs):
        if self.product_id is None and self.created_date and self.id:
            self.product_id = self.created_date.strftime('SIPPIT%Y29%m01%d') + str(self.id)
        return super().save(*args, **kwargs)


class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=200)
    email = models.EmailField(max_length=90)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)   
    additional_info=models.TextField() 
    date=models.DateTimeField(default=timezone.now)
    phone = models.IntegerField()
    amount=models.CharField(max_length=100)
    payment_id=models.CharField(max_length=200,null=True,blank=True)
    paid=models.BooleanField(default=False,null=True)
    
    def __str__(self):
        return self.email

class Order_item(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.CharField(max_length=200)
    image=models.ImageField(upload_to='images/Order_item')
    quantity=models.IntegerField()
    price=models.CharField(max_length=150)
    total=models.CharField(max_length=180)

    def __str__(self):
        return self.order.user.username

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    delivered=models.BooleanField(default=False)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."

class Images(models.Model):
    image=models.ImageField(upload_to='images')
    product=models.ForeignKey(Product,on_delete=models.CASCADE)


