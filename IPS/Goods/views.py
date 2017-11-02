from django.shortcuts import render, get_object_or_404
from .models import Goods
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def GoodsView(request, page_number = 1):
    goods_list = Goods.objects.order_by('id')
    paginator = Paginator(goods_list, 20)
    page = request.GET.get('page')
    try:
        goods = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        goods = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        goods = paginator.page(paginator.num_pages)
    return render(request, 'goods.html', {'goods': goods},)

def GoodView(request, Goods_id):
    good = get_object_or_404(Goods, pk=Goods_id)
    return render(request, 'good.html', {'good': good})


def mymethod(request):
    print('Dont work :( ')
    if (request.POST.get('mybtn')):
        print('Works!')
    return render(request, 'goods.html')
