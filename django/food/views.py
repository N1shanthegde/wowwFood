import json
from django.shortcuts import redirect, render
from django.http import Http404, HttpResponse
from food.models import Burger, Pizza, Order, Item, Sandwich, Momos
from .forms import NewUserForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import random

def randdomOrderNumber(length):
    sample = 'ABCDEFGHIJ1234567890'
    number0 = ''.join((random.choice(sample) for i in range(length)))
    return number0

def index(request):
    request.session.set_expiry(0)
    ctx = {'active_link': 'index'}
    return render(request, 'food/index.html', ctx)

def pizza(request):
    request.session.set_expiry(0)
    pizzas = Pizza.objects.all()
    ctx = {'pizzas': pizzas}
    return render(request, 'food/pizza.html', ctx)

def burger(request):
    request.session.set_expiry(0)
    burgers = Burger.objects.all()
    ctx = {'burgers': burgers}
    return render(request, 'food/burgers.html', ctx)

def moms(request):
    request.session.set_expiry(0)
    momss = Momos.objects.all()
    ctx = {'momss': momss}
    return render(request, 'food/moms.html', ctx)

def sandwich(request):
    request.session.set_expiry(0)
    sandwichs = Sandwich.objects.all()
    ctx = {'sandwichs': sandwichs}
    return render(request, 'food/sandwich.html', ctx)



@csrf_exempt
def order(request):
    request.session.set_expiry(0)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        request.session['note'] = request.POST.get('note')
        request.session['order'] = request.POST.get('orders')
        request.session['bill'] = request.POST.get('bill')
        orders = json.loads(request.session['order'])
        randomNum = randdomOrderNumber(6)
        
        while Order.objects.filter(number = randomNum).count() > 0:
            randomNum = randdomOrderNumber(6)
            
        if request.user.is_authenticated:
            order = Order(customer = request.user, 
                          number = randdomOrderNumber(6), 
                          bill = float(request.session['bill']), 
                          note= request.session['note'],
                        )
            order.save()
            request.session['orderNum'] = order.number
            for article in orders:
                item = Item(
                    order = order,
                    name = article[0],
                    price = float(article[2]),
                    size = article[1]
                )
                item.save()
                
    ctx = {'active_link': 'order'}
    return render(request, 'food/order.html', ctx)

# def success(request):
#     orderNum = request.session['orderNum']
#     bill = request.session['bill']
#     items = Item.objects.filter(order__number = orderNum)
#     ctx = {'orderNum':orderNum, 'bill':bill, 'items':items}
#     return render(request, 'food/success.html', ctx)

def success(request):
    try:
        orderNum = request.session.get('orderNum')
        bill = request.session.get('bill')
        
        if not orderNum or not bill:
            # If session variables are not set, redirect to an appropriate page
            return redirect('food:order')
        
        try:
            order = Order.objects.get(number=orderNum)
        except Order.DoesNotExist:
            # If the order doesn't exist, raise a 404 error
            raise Http404("Order does not exist")
        
        items = Item.objects.filter(order=order)
        
        ctx = {'orderNum': orderNum, 'bill': bill, 'items': items}
        return render(request, 'food/success.html', ctx)
    
    except Exception as e:
        # Handle any unexpected errors
        print(f"Unexpected error in success view: {str(e)}")
        return redirect('food:index')
    
    # return render(request, 'food/success.html', ctx)
    

def signup(request):
    ctx = {}
    if request.POST:
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            ctx['form'] = form
    else:
        form= NewUserForm()
        ctx['form'] =  form
    return render(request, 'food/signup.html', ctx)

def logIn(request):
    if request.POST:
        username =  request.POST.get('username')
        pwd = request.POST.get('password')
        user = authenticate(request, username = username, password= pwd)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'username and password don not match!!')
    ctx = {'active_link': 'login'}
    return render(request, 'food/login.html', ctx)

def logOut(request):
    logout(request)
    return redirect('index')


def contactus(request):
    return render(request, 'food/contactus.html')

def aboutus(request):
    return render(request, 'food/aboutus.html')