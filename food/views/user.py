from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.core.paginator import Paginator
from django.http import JsonResponse

from hashlib import sha1




def register(request):

    context = {
        'title': '用户注册',
    }
    return render(request, 'templates/register.html', context)


def register_handle(request):

    username = request.POST.get('user_name')
    password = request.POST.get('pwd')
    confirm_pwd = request.POST.get('confirm_pwd')
    email = request.POST.get('email')

    # 判断两次密码一致性
    if password != confirm_pwd:
        return redirect('/user/register/')
    # 密码加密
    s1 = sha1()
    s1.update(password.encode('utf8'))
    encrypted_pwd = s1.hexdigest()

    # 创建对象
    UserInfo.objects.create(uname=username, upwd=encrypted_pwd, uemail=email)
    # 注册成功
    context = {
        'title': '用户登陆',
        'username': username,
    }
    return render(request, 'templates/login.html', context)


def register_exist(request):
    username = request.GET.get('uname')
    count = UserInfo.objects.filter(uname=username).count()
    return JsonResponse({'count': count})


def login(request):
    uname = request.COOKIES.get('uname', '')
    context = {
        'title': '用户登陆',
        'error_name': 0,
        'error_pwd': 0,
        'uname': uname,
    }
    return render(request, 'templates/login.html', context)


def login_handle(request):  # 没有利用ajax提交表单
    # 接受请求信息
    uname = request.POST.get('username')
    upwd = request.POST.get('pwd')
    jizhu = request.POST.get('jizhu', 0)
    users = UserInfo.objects.filter(uname=uname)
    if len(users) == 1:  # 判断用户密码并跳转
        s1 = sha1()
        s1.update(upwd.encode('utf8'))
        if s1.hexdigest() == users[0].upwd:
            url = request.COOKIES.get('url', '/')
            red = HttpResponseRedirect(url)  # 继承与HttpResponse 在跳转的同时 设置一个cookie值
            # 是否勾选记住用户名，设置cookie
            if jizhu != 0:
                red.set_cookie('uname', uname)
            else:
                red.set_cookie('uname', '', max_age=-1)  # 设置过期cookie时间，立刻过期
            request.session['user_id'] = users[0].id
            request.session['user_name'] = uname
            return red
        else:
            context = {
                'title': '用户名登陆',
                'error_name': 0,
                'error_pwd': 1,
                'uname': uname,
                'upwd': upwd,
            }
            return render(request, 'templates/login.html', context)
    else:
        context = {
            'title': '用户名登陆',
            'error_name': 1,
            'error_pwd': 0,
            'uname': uname,
            'upwd': upwd,
        }
        return render(request, 'templates/login.html', context)


def logout(request):  # 用户登出
    request.session.flush()  # 清空当前用户所有session
    return redirect(reverse("common:index"))
