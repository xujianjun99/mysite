"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import HttpResponse, redirect, render

def login(request):
    '''
    处理用户请求，并返回内容
    :param request:用户请求相关的所有信息（对象）
    '''
    # return HttpResponse("login.html")
    print(request.method)
    if request.method=='GET':
        print(request.method)
        user = request.GET.get('user')
        pwd = request.GET.get('pwd')
        print(f'用户名：{user},密码：{pwd}')        
    else:
        print(request.method)
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        print(f'用户名：{user},密码：{pwd}')
    if (user=='root') & (pwd=='123'):
        return redirect('http://baidu.com')
    else:
        return render(request,'login.html')
    # return render(request,'login.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',login)
]
