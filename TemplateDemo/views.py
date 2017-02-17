from django.shortcuts import render


# Create your views here.
def home(request):
    string = u"我在学习 Django 哦！建设网站"
    return render(request, 'home.html', {'string': string})
