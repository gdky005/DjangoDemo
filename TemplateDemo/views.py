from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    # string = u"我在学习 Django 哦！建设网站"
    # TutorialList = ['HTML', 'CSS', 'jQuery', 'Python', 'Django']
    # info_dict = {'site': 'WangQing', 'content': "正在学习 Python 的 Django"}

    # List = map(str, range(100))
    # List = None

    var = 40

    return render(request, 'home.html', {'var': var})


def add(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))
