from django.db import models

# Create your models here.

class Log(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20,unique=True)
    role = models.CharField(max_length=10)
    def __str__(self):
        return self.username

class brookuser(models.Model):
    fullname = models.CharField(max_length=20)
    housename= models.CharField(max_length=30)
    roadname = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    post = models.CharField(max_length=20)
    pincode = models.CharField(max_length=6)
    email = models.EmailField(max_length=40)
    phone_number = models.CharField(max_length=10)
    log_id = models.OneToOneField(Log, on_delete=models.CASCADE)
    role = models.CharField(max_length=10)
    userstatus = models.CharField(max_length=10)
    def __str__(self):
        return self.fullname

class complaint(models.Model):

    user = models.ForeignKey(brookuser, on_delete=models.CASCADE)
    product = models.CharField(max_length=500)
    complaint = models.CharField(max_length=500)
    date = models.DateField()
    replay= models.CharField(max_length=500,default='No Replay')
    complaint_status = models.CharField(max_length=10)
    def __str__(self):
        return self.complaint



class category(models.Model):
    category_name = models.CharField(max_length=50)
    category_status = models.CharField(max_length=10)

    def __str__(self):
        return self.category_name


class product(models.Model):
    category= models.CharField(max_length=50)
    product_name = models.CharField(max_length=50)
    price = models.IntegerField()
    GST = models.IntegerField()
    product_price = models.IntegerField()
    product_details = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images')
    stock = models.CharField(max_length=500)
    product_status = models.CharField(max_length=10)

    def __str__(self):
        return self.product_name

class cart(models.Model):
    user = models.ForeignKey(brookuser, on_delete=models.CASCADE)
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    quantity = models.CharField(max_length=500)
    total_price= models.CharField(max_length=500)
    cart_status = models.CharField(max_length=10)


# class order(models.Model):

#     product=models.ForeignKey(product,on_delete=models.CASCADE)
#     # image = models.CharField(max_length=200)
#     Quantity = models.CharField(max_length=500)
#     price= models.IntegerField()
#     date=models.CharField(max_length=20)
#     time=models.CharField(max_length=20)
#     order_status = models.CharField(max_length=10)

#     def __str__(self):
#         return self.product

# class bill(models.Model):
#     total_amount = models.CharField(max_length=50)
#     date=models.CharField(max_length=20)
#     time=models.CharField(max_length=20)
#     log_id = models.OneToOneField(Log, on_delete=models.CASCADE)
#     role = models.CharField(max_length=10)
#     userstatus = models.CharField(max_length=10)

#     def __str__(self):
#         return self.total_amount

# class payment(models.Model):
#     bank = models.CharField(max_length=50)
#     log_id = models.OneToOneField(Log, on_delete=models.CASCADE)
#     role = models.CharField(max_length=10)
#     userstatus = models.CharField(max_length=10)

#     def __str__(self):
#         return self.bank



# class feedback(models.Model):
#     feedback = models.CharField(max_length=500)
#     user = models.ForeignKey(brookuser, on_delete=models.CASCADE)
#     product=models.ForeignKey(product,on_delete=models.CASCADE)
#     date=models.CharField(max_length=20)
#     time=models.CharField(max_length=20)

#     def __str__(self):
#         return self.feedback
