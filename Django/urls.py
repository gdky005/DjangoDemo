"""Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from Demo import views as demo_views
from TemplateDemo import views as template_views

# 网址入口，关联到对应的views.py中的一个函数


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$', demo_views.index),
    # url(r'^$', demo_views.index2),
    url('^add/$', demo_views.add, name='add'),
    url(r'^add/(\d+)/(\d+)/$', demo_views.add2, name='add2'),
    url(r'^new_add/(\d+)/(\d+)/$', demo_views.add2, name='add2'),
    # url(r'^$', demo_views.home, name='home'),
    url(r'^$', template_views.home, name='home'),
    url(r'^add/(\d+)/(\d+)/$', template_views.add, name='add'),

]
