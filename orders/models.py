from django.db import models

# Create your models here.
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE)  
	coupon=	models.IntegerField(default=0)

	def __str__(self):
		return self.user.username

class Other(models.Model):
	name=models.CharField(max_length=64,blank=True)
	category=models.CharField(max_length=64,blank=True)
	size=models.CharField(max_length=64,blank=True)	
	price=models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		return f"${self.price} -- {self.category}: {self.size} {self.name}"

class Sub(models.Model):
	name=models.CharField(max_length=64,blank=True)
	size=models.CharField(max_length=64,blank=True)
	price=models.DecimalField(max_digits=5, decimal_places=2)
	toppings=models.ManyToManyField('SubTopping',blank=True)

	def __str__(self):
		toppingstring=""
		for i in self.toppings.all():
			toppingstring+= f"{i.name}, "
		toppingstring=toppingstring[0:-2]
		if len(self.toppings.all())>0:
			toppingstring="-Extra: "+toppingstring
		return f"${self.price} -- {self.size} {self.name} Sub{toppingstring}"

class SubTopping(models.Model):
    name=models.CharField(max_length=64)
    price=models.DecimalField(default=0.5, max_digits=3,decimal_places=2)

    def __str__(self):
        return f"{self.name}"

class SubOrder(models.Model):
	name=models.CharField(max_length=64,blank=True)
	size=models.CharField(max_length=64,blank=True)
	price=models.DecimalField(max_digits=5, decimal_places=2)
	##for others
	category=models.CharField(max_length=64,blank=True)
	##for subs
	toppings=models.ManyToManyField('SubTopping',blank=True)
	##for pizzas
	ptype=models.CharField(max_length=64,blank=True)
	ntoppings=models.IntegerField(default=0)
	ptoppings=models.ManyToManyField('PizzaTopping',blank=True)

	orderstatus=models.CharField(max_length=64,default="pending")
	customer=models.ForeignKey(User, on_delete=models.CASCADE,related_name="suborder",null=True)

	def __str__(self):
		# pizza
		if self.ptype!="":
			toppingstring=""
			for i in self.ptoppings.all():
				toppingstring+= f"{i.name}, "
			toppingstring=toppingstring[0:-2]
			return f"${self.price} -- {self.size} {self.ptype} {self.name} Pizza - Toppings: {toppingstring}"
		#sub
		elif self.category=="":			
			toppingstring=""
			for i in self.toppings.all():
				toppingstring+= f"{i.name}, "
			toppingstring=toppingstring[0:-2]
			if len(self.toppings.all())>0:
				toppingstring=" - Extra: "+toppingstring
			return f"${self.price} -- {self.size} {self.name} Sub{toppingstring}"
		#everything else
		else:
			return f"${self.price} -- {self.category}: {self.size} {self.name}"

class Pizza(models.Model):
	name=models.CharField(max_length=64,blank=True)
	size=models.CharField(max_length=64,blank=True)
	price=models.DecimalField(max_digits=5, decimal_places=2)
	ptype=models.CharField(max_length=64,blank=True)
	ntoppings=models.IntegerField()
	ptoppings=models.ManyToManyField('PizzaTopping',blank=True)

	def __str__(self):
		toppingstring=""
		for i in self.ptoppings.all():
			toppingstring+= f"{i.name}, "
		toppingstring=toppingstring[0:-2]
		return f"${self.price} -- {self.size} {self.ptype} {self.name} Pizza - Toppings: {toppingstring}"

class PizzaTopping(models.Model):
	name=models.CharField(max_length=64,blank=True)

	def __str__(self):
		return self.name