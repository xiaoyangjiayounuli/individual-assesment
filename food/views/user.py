from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from food.forms import UserLoginForm


def register(request):
    messages = ''
    if request.method=='POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('telephone')
        repeat_judge = User.objects.filter(username=username)
        if password1 != password2:
            messages = 'Error, passwords do not match, please try again.'
        elif repeat_judge:
            messages = 'Error, username already existed, please try again.'
        else:
            User.objects.create_user(username=username, password=password1).save()
            Information.objects.create(username=username, telephone=telephone).save()
            return redirect('login')
    return render(request, 'register.html', {'messages': messages})



def user_login(request):
    if request.method == 'POST':
        user_login_form = UserLoginForm(data=request.POST)
        if user_login_form.is_valid():
            # .cleaned_data 清洗出合法数据
            data = user_login_form.cleaned_data
            # 检验账号、密码是否正确匹配数据库中的某个用户
            # 如果均匹配则返回这个 user 对象
            user = authenticate(username=data['username'], password=data['password'])
            if user:
                # 将用户数据保存在 session 中，即实现了登录动作
                login(request, user)
                return redirect("food:food_list")
            else:
                return HttpResponse("The account number or password has been entered incorrectly. Please re-enter~")
        else:
            return HttpResponse("Account number or password input is not legal")
    elif request.method == 'GET':
        user_login_form = UserLoginForm()
        context = { 'form': user_login_form }
        return render(request, 'login.html', context)
    else:
        return HttpResponse("Please use GET or POST to request data")


def logout(request):  # 用户登出
    request.session.flush()  # 清空当前用户所有session
    return redirect(reverse("food:index"))
