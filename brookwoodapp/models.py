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
    image = models.ImageField(upload_to='images')
    category_status = models.CharField(max_length=10)

    def __str__(self):
        return self.category_name


class product(models.Model):
    category= models.ForeignKey(category, on_delete=models.CASCADE)
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
    # image = models.ImageField(upload_to='images')
    category = models.CharField(max_length=10)


class Review(models.Model):
    user = models.ForeignKey(brookuser, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=500)
    rating = models.CharField(max_length=50)
    date = models.DateField()
    review_status = models.CharField(max_length=10)

    def __str__(self):
        return self.feedback


class order(models.Model):
    user=models.ForeignKey(brookuser,on_delete=models.CASCADE)
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    quantity = models.CharField(max_length=500)
    price= models.IntegerField()
    order_status = models.CharField(max_length=10)

   

# class bill(models.Model):
#     total_amount = models.CharField(max_length=50)
#     date=models.CharField(max_length=20)
#     time=models.CharField(max_length=20)
#     log_id = models.OneToOneField(Log, on_delete=models.CASCADE)
#     role = models.CharField(max_length=10)
#     userstatus = models.CharField(max_length=10)

#     def __str__(self):
#         return self.total_amount

class payment(models.Model):
    user=models.ForeignKey(brookuser,on_delete=models.CASCADE)
    orders=models.ForeignKey(order,on_delete=models.CASCADE)
    amount = models.CharField(max_length=10)
    date = models.DateField()
    paymentstatus = models.CharField(max_length=10)





# class feedback(models.Model):
#     feedback = models.CharField(max_length=500)
#     user = models.ForeignKey(brookuser, on_delete=models.CASCADE)
#     product=models.ForeignKey(product,on_delete=models.CASCADE)
#     date=models.CharField(max_length=20)
#     time=models.CharField(max_length=20)

#     def __str__(self):
#         return self.feedback
