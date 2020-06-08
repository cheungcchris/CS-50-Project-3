from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import random

from .models import Profile,Other,Sub,SubTopping,SubOrder,Pizza,PizzaTopping

def index(request):
    if not request.user.is_authenticated:
        return render(request, "orders/index.html", {"message": None})
    context = {
        "user": request.user,
        "coupon":Profile.objects.get(user=request.user).coupon
    }

    return render(request, "orders/user.html", context)

def menu(request):
    context={
        "pizza":Pizza.objects.all().order_by('ptype'),
        "pizzatopping":PizzaTopping.objects.all(),
        "ptypes":["Regular","Sicilian"],
        "sub":Sub.objects.all().order_by('name','-size'),
        "subtopping":SubTopping.objects.all(),
        "pasta":Other.objects.filter(category="Pasta"),
        "salad":Other.objects.filter(category="Salad"),
        "dinnerplatter":Other.objects.filter(category="Dinner Platter").order_by('name','-size'),
        "user":request.user,
        "cart":User.objects.get(pk=request.user.id).suborder.all().filter(orderstatus="pending"),
        "coupon":Profile.objects.get(user=request.user).coupon
        }
    
    return render(request,"orders/menu.html",context=context)

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "orders/index.html", {"message": "Invalid credentials."})

def logout_view(request):
    logout(request)
    return render(request, "orders/index.html", {"message": "Logged out."})

def signup_view(request):
    return render(request, "orders/signup.html")

def register_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    firstname = request.POST["firstname"]
    lastname = request.POST["lastname"]
    email = request.POST["email"]

    user = User.objects.create_user(username, email, password)
    user.first_name=firstname
    user.last_name=lastname
    user.save()
    
    return render(request, "orders/index.html", {"message": "User Registered"})

def addtocart(request):
    item=request.POST["addtocart"]

    curritem=Other.objects.get(pk=item)
    newitem=SubOrder(name=curritem.name,
                     size=curritem.size,
                     category=curritem.category,
                     price=curritem.price,
                     customer=User.objects.get(pk=request.user.id)
                     )
    newitem.save()

    context={
        "pizza":Pizza.objects.all().order_by('ptype'),
        "pizzatopping":PizzaTopping.objects.all(),
        "ptypes":["Regular","Sicilian"],
        "sub":Sub.objects.all().order_by('name','-size'),
        "subtopping":SubTopping.objects.all(),
        "pasta":Other.objects.filter(category="Pasta"),
        "salad":Other.objects.filter(category="Salad"),
        "dinnerplatter":Other.objects.filter(category="Dinner Platter").order_by('name','-size'),
        "user":request.user,
        "cart":User.objects.get(pk=request.user.id).suborder.all().filter(orderstatus="pending"),
        "coupon":Profile.objects.get(user=request.user).coupon
        }
    return render(request,"orders/menu.html",context=context)

def addtocartsub(request): 
    item=request.POST["addtocartsub"]
    toppings=request.POST.getlist("subtopping")
    currsub=Sub.objects.get(pk=item)
    
    newsub=SubOrder(name=currsub.name,
                    size=currsub.size,
                    price="{:.2f}".format(float(currsub.price)+len(toppings)*0.5),
                    customer=User.objects.get(pk=request.user.id))
    newsub.save()

    for i in toppings:
        toppingid=SubTopping.objects.get(name=i).id
        newsub.toppings.add(SubTopping.objects.get(pk=toppingid))

    newsub.save()
    
    context={
        "pizza":Pizza.objects.all().order_by('ptype'),
        "pizzatopping":PizzaTopping.objects.all(),
        "ptypes":["Regular","Sicilian"],
        "sub":Sub.objects.all().order_by('name','-size'),
        "subtopping":SubTopping.objects.all(),
        "pasta":Other.objects.filter(category="Pasta"),
        "salad":Other.objects.filter(category="Salad"),
        "dinnerplatter":Other.objects.filter(category="Dinner Platter").order_by('name','-size'),
        "user":request.user,
        "cart":User.objects.get(pk=request.user.id).suborder.all().filter(orderstatus="pending"),
        "coupon":Profile.objects.get(user=request.user).coupon
        }
    return render(request,"orders/menu.html",context=context)
    
def addtocartpizza(request):
    item=request.POST["addtocartpizza"]
    toppings=request.POST.getlist("pizzatopping")
    currpizza=Pizza.objects.get(pk=item)
    newpizza=SubOrder(name=currpizza.name,
                      size=currpizza.size,
                      price=currpizza.price,
                      ptype=currpizza.ptype,
                      ntoppings=currpizza.ntoppings,
                      customer=User.objects.get(pk=request.user.id)
                      )
    newpizza.save()
    for i in toppings:
        toppingid=PizzaTopping.objects.get(name=i).id
        newpizza.ptoppings.add(PizzaTopping.objects.get(pk=toppingid))
    newpizza.save()

    context={
        "pizza":Pizza.objects.all().order_by('ptype'),
        "pizzatopping":PizzaTopping.objects.all(),
        "ptypes":["Regular","Sicilian"],
        "sub":Sub.objects.all().order_by('name','-size'),
        "subtopping":SubTopping.objects.all(),
        "pasta":Other.objects.filter(category="Pasta"),
        "salad":Other.objects.filter(category="Salad"),
        "dinnerplatter":Other.objects.filter(category="Dinner Platter").order_by('name','-size'),
        "user":request.user,
        "cart":User.objects.get(pk=request.user.id).suborder.all().filter(orderstatus="pending"),
        "coupon":Profile.objects.get(user=request.user).coupon
        }    
    return render(request,"orders/menu.html",context=context)

def removefromcart(request):
    itemid=request.POST["removefromcart"]
    SubOrder.objects.get(pk=itemid).delete()

    context={
        "pizza":Pizza.objects.all().order_by('ptype'),
        "pizzatopping":PizzaTopping.objects.all(),
        "ptypes":["Regular","Sicilian"],
        "sub":Sub.objects.all().order_by('name','-size'),
        "subtopping":SubTopping.objects.all(),
        "pasta":Other.objects.filter(category="Pasta"),
        "salad":Other.objects.filter(category="Salad"),
        "dinnerplatter":Other.objects.filter(category="Dinner Platter").order_by('name','-size'),
        "user":request.user,
        "cart":User.objects.get(pk=request.user.id).suborder.all().filter(orderstatus="pending"),
        "coupon":Profile.objects.get(user=request.user).coupon
        }    
    return render(request,"orders/menu.html",context=context)

def placeorder(request):
    for i in User.objects.get(pk=request.user.id).suborder.all():
        i.orderstatus="complete"
        i.save()

    ##coupon
    rollcoupon=random.randint(1,100)
    userprofile=Profile.objects.get(user=request.user)
    print(rollcoupon)
    if 1<rollcoupon<40:
        userprofile.coupon=5
    elif 41<rollcoupon<70:
        userprofile.coupon=10
    elif 71<rollcoupon<90:
        userprofile.coupon=15
    else:
        userprofile.coupon=20
    userprofile.save()    
    print(userprofile.coupon)
    context = {
        "user": request.user,
        "message":", your order has been placed!",
        "coupon":Profile.objects.get(user=request.user).coupon
    }
    return render(request, "orders/user.html", context)
