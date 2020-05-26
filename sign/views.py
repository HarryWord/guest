from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models import Event,Guest

# Create your views here.
def index(request):
    # return HttpResponse("Hello Django!")
    return render(request,"index.html")

def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user) # 登录
            # return HttpResponse('Login success!')
            # return HttpResponseRedirect('/event_manage/')
            # response.set_cookie('user',username,3600) # 添加浏览器cookie
            request.session['user'] = username # 将session信息记录到浏览器
            response = HttpResponseRedirect('/event_manage/')
            return response
        else:
            return render(request,'index.html',{'error':'username or password error!'})

#发布会管理
@login_required
def event_manage(request):
    # username = request.COOKIES.get('user','') # 读取浏览器cookie
    event_list = Event.objects.all()
    username = request.session.get('user','') #读取浏览器session
    return render(request,'event_manage.html',{"user":username,"events":event_list})

# 发布会名称搜索
@login_required
def search_name(request):
    username = request.session.get('user','')
    search_name = request.GET.get("name","")
    event_list = Event.objects.filter(name__contains=search_name)
    return render(request,"event_manage.html",{"user":username,"events":event_list})

# 嘉宾管理
@login_required
def guest_manage(request):
    username = request.session.get('user','')
    guest_list = Guest.objects.all()
    return render(request,"guest_manage.html",{"user":username,"guests":guest_list})

def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user) # 登录
            # return HttpResponse('Login success!')
            # return HttpResponseRedirect('/event_manage/')
            # response.set_cookie('user',username,3600) # 添加浏览器cookie
            request.session['user'] = username # 将session信息记录到浏览器
            response = HttpResponseRedirect('/event_manage/')
            return response
        else:
            return render(request,'index.html',{'error':'username or password error!'})

#发布会管理
@login_required
def event_manage(request):
    # username = request.COOKIES.get('user','') # 读取浏览器cookie
    event_list = Event.objects.all()
    username = request.session.get('user','') #读取浏览器session
    return render(request,'event_manage.html',{"user":username,"events":event_list})

# 发布会名称搜索
@login_required
def search_name(request):
    username = request.session.get('user','')
    search_name = request.GET.get("name","")
    event_list = Event.objects.filter(name__contains=search_name)
    return render(request,"event_manage.html",{"user":username,"events":event_list})

# 嘉宾管理
@login_required
def guest_manage(request):
    username = request.session.get('user','')
    guest_list = Guest.objects.all()
    return render(request,"guest_manage.html",{"user":username,"guests":guest_list})