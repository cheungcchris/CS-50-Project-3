from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("menu", views.menu, name="menu"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("signup", views.signup_view, name="signup"),
    path("register", views.register_view, name="register"),
    path("addtocart", views.addtocart, name="addtocart"),
    path("addtocartsub", views.addtocartsub, name="addtocartsub"),
    path("addtocartpizza", views.addtocartpizza, name="addtocartpizza"),
    path("removefromcart", views.removefromcart, name="removefromcart"),
    path("placeorder", views.placeorder, name="placeorder")
]
