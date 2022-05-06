from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from food.forms import UserLoginForm,UserRegisterForm



def user_register(request):
    if request.method == 'POST':
        user_register_form = UserRegisterForm(data=request.POST)
        if user_register_form.is_valid():
            new_user = user_register_form.save(commit=False)
            # 设置密码
            new_user.set_password(user_register_form.cleaned_data['password'])
            new_user.save()
            # 保存好数据后立即登录并返回博客列表页面
            login(request, new_user)
            return redirect("food:food_list")
        else:
            return HttpResponse("The registration form was entered incorrectly. Please re-enter~")
    elif request.method == 'GET':
        user_register_form = UserRegisterForm()
        context = { 'form': user_register_form }
        return render(request, 'register.html', context)
    else:
        return HttpResponse("Please use GET or POST to request data")


def user_login(request):
    if request.method == 'POST':
        user_login_form = UserLoginForm(data=request.POST)
        if user_login_form.is_valid():
            # .cleaned_data Cleaning out legitimate data
            data = user_login_form.cleaned_data
            # Check if the account and password match a user in the database
            # If they all match, return the user object
            user = authenticate(username=data['username'], password=data['password'])
            if user:
                # The user data is saved in the session, i.e. the login action is implemented
                login(request, user)
                return redirect("food:index")
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


def logout(request):  # logout
    request.session.flush()  # clean current user all session
    return redirect('food:index')
