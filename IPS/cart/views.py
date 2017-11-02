from django.shortcuts import render, get_object_or_404
from .models import Cart, MyUser, Goods
from django.db.models import Sum
from django.http import HttpResponseRedirect
from .forms import CartForm

def CartAdd(request, cart_id):
    man = request.user.id
    myUser = MyUser.objects.filter(id=man)
    myUser = myUser[0]
    myUser.cartids = myUser.cartids +"::"+ cart_id
    myUser.save()
    good = Goods.objects.filter(id=cart_id)
    good = good[0]
    return render (request, 'cartadd.html', {'cart_id': cart_id})

def CartView(request):
    man = request.user.id
    goods = Goods.objects.all()
    myUser = MyUser.objects.filter(id=man)
    myUser = myUser[0]
    aza = myUser.cartids.split('::')
    aza = aza[1::]
    counts = []
    for azaid in aza:
        n = aza.count(azaid)
        counts.append(n)
        while n > 1:
            n = n - 1
            aza.remove(azaid)
    data = []
    for i in range(len(goods)):
        data.append([goods[i],counts[i]])
    summ = 0
    for dt in data:
        summ += dt[0].good_price*dt[1]
    return render(request, 'cart.html', {'data':data, 'summ':summ})

def ClearCart(request):
    man = request.user.id
    goods = Goods.objects.all()
    myUser = MyUser.objects.filter(id=man)
    myUser = myUser[0]
    myUser.cartids = [0]
    myUser.save()
    return HttpResponseRedirect('/goods/')

def get_order(request):
    form = CartForm()
    return render(request, 'order.html', {'form': form})