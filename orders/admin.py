from django.contrib import admin

# Register your models here.
from .models import Profile, Other,  Sub, SubTopping, SubOrder, Pizza, PizzaTopping
admin.site.register(Profile)
admin.site.register(Other)
admin.site.register(Sub)
admin.site.register(SubTopping)
admin.site.register(SubOrder)
admin.site.register(Pizza)
admin.site.register(PizzaTopping)
