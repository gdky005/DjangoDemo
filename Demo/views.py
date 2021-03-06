from audioop import reverse

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# 处理用户发出的请求，从urls.py中对应过来, 通过渲染templates中的网页可以将显示内容，比如登陆后的用户名，用户请求的数据，输出到网页。

def index2(request):
    return HttpResponse("欢迎光临我的网页！")


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)

    return HttpResponse(str(c))


def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))


def index(request):
    return render(request, 'Demo/home.html')


def old_add2_redirect(request, a, b):
    return HttpResponseRedirect(
        reverse('add2', args=(a, b))
    )


def home(request):
    return render(request, "Demo/home.html")