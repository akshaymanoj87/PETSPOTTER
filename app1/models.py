from django.db import models

# Create your models here.
class register (models.Model):
	name=models.CharField(max_length=100, default='')
	email=models.CharField( max_length=100, default='')
	password=models.CharField(max_length=32, default='')
	phone=models.CharField(max_length=32, default='')
	address=models.CharField(max_length=100, default='')
	status1=models.CharField(max_length=100, default='')
	Image=models.ImageField(upload_to='image',default='')
	type=models.CharField(max_length=100, default='')


class add_pets(models.Model):
	pid=models.ForeignKey(register,on_delete=models.CASCADE)
	name=models.CharField(max_length=100, default='')
	Category=models.CharField(max_length=100, default='')
	Breed=models.CharField(max_length=100, default='')
	Age=models.CharField(max_length=100, default='')
	Colour=models.CharField(max_length=100, default='')
	size=models.IntegerField(default=0)
	Vaccination=models.CharField(max_length=100, default='')
	Description=models.CharField(max_length=100, default='')
	Price=models.CharField(max_length=100, default='')
	status=models.CharField(max_length=100, default='')
	Image=models.ImageField(upload_to='pets')
	type=models.CharField(max_length=100, default='')
	availableqty=models.CharField(max_length=100, default='')
	rating=models.FloatField(max_length=100,default=0)

class add_food(models.Model):
	fid=models.ForeignKey(register,on_delete=models.CASCADE,default="")
	name=models.CharField(max_length=100, default='')
	Category=models.CharField(max_length=100, default='')
	quantity=models.CharField(max_length=100, default='')
	Description=models.CharField(max_length=100, default='')
	Price=models.CharField(max_length=100, default='')
	status=models.CharField(max_length=100, default='')
	Image=models.ImageField(upload_to='food')
	availableqty=models.CharField(max_length=100, default='')
	rating=models.FloatField(max_length=100,default=0)


class cart_tb(models.Model):
	userid=models.ForeignKey(register, on_delete=models.CASCADE)
	pid=models.ForeignKey(add_pets,on_delete=models.CASCADE,default="",null=True)
	fid=models.ForeignKey(add_food,on_delete=models.CASCADE,default="",null=True)
	quantity=models.CharField(max_length=100,default='')
	shipping=models.CharField(max_length=100,default='')
	total=models.CharField(max_length=100,default='')
	unitprice=models.CharField(max_length=100,default='')
	date=models.CharField(max_length=100,default='')
	status=models.CharField(max_length=100,default='Pending')
	item=models.CharField(max_length=100,default='')
	shopid=models.IntegerField(default=0)
	shoppay=models.CharField(max_length=100,default='pending')
	

class payment_tb(models.Model):
	userid=models.ForeignKey(register, on_delete=models.CASCADE)
	amount=models.CharField(max_length=100,default='')
	status=models.CharField(max_length=100,default='')
	date=models.CharField(max_length=100,default='')
	

class paymenttoshop_tb(models.Model):
	shopid=models.ForeignKey(register, on_delete=models.CASCADE)
	amount=models.CharField(max_length=100,default='')
	date=models.CharField(max_length=100,default='')
	cartid=models.ForeignKey(cart_tb, on_delete=models.CASCADE,default='')

class vetenery_tb(models.Model):
	regid=models.ForeignKey(register, on_delete=models.CASCADE)
	qualification=models.CharField(max_length=100,default='')
	experience=models.CharField(max_length=100,default='')
	status=models.CharField(max_length=100, default='pending')
	days=models.CharField(max_length=100,default='')
	time=models.CharField(max_length=100,default='')
	clinic=models.CharField(max_length=100,default='')

class review_tb(models.Model):
	userid=models.ForeignKey(register, on_delete=models.CASCADE)
	pid=models.ForeignKey(add_pets,on_delete=models.CASCADE,null=True)
	fid=models.ForeignKey(add_food,on_delete=models.CASCADE,null=True)
	item=models.CharField(max_length=100,default='')
	rating=models.CharField(max_length=100,default='')
	cartid=models.ForeignKey(cart_tb, on_delete=models.CASCADE,default='')