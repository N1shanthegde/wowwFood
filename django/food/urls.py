from django.urls import path
from . import views
app_name = 'food'

urlpatterns = [
    path('pizza', views.pizza, name='pizza'),
    path('burgers', views.burger, name='burger'),
    path('moms', views.moms, name='moms'),
    path('sandwich', views.sandwich, name='sandwich'),
    path('order', views.order, name='order'),
    path('success', views.success, name='success'),
    path('signup', views.signup, name='signup'),
    path('login', views.logIn, name='login'),
    path('logout', views.logOut, name='logout'),
    path('contactus', views.contactus, name='contactus'),
    path('aboutus', views.aboutus, name='aboutus'),
]
