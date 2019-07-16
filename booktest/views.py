# coding=utf-8
from django.shortcuts import render
from models import *
from django.db.models import Max, F, Q

# Create your views here.


def index(request):
    # l = BookInfo.books1.filter(heroinfo__content__contains='六')
    # l = BookInfo.books1.filter(pk__lte=3)
    # max = BookInfo.books1.aggregate(Max('pub_date'))
    # l = BookInfo.books1.filter(read__gt=F('comment')) # F对象，当需要在不同的列间做运算时，需要用到F对象(等于是获取筛选到的当前对象)
    # l = BookInfo.books1.filter(pk__lt=4, title__contains='1')
    # l = BookInfo.books1.filter(pk__lt=4).filter(title__contains='1')
    l = BookInfo.books1.filter(Q(pk__lt=4) | Q(title__contains='1'))  # Q对象用于字段间 进行比较运算符时，如or，~Q()取反等的关系
    context = {'list': l
                    # ,"max": max

               }
    return render(request, 'booktest/index.html', context)


def details(request, id):
    b = BookInfo.books1.get(pk=id)
    hero_list = b.heroinfo_set.all()
    print hero_list
    context = {'list': hero_list}
    return render(request, 'booktest/details.html', context)


def area(request):
    area = AreaInfo.objects.get(pk=130100)
    return render(request, 'booktest/area.html', {'area': area})
