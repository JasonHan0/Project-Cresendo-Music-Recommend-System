from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login # login함수와 이름이 겹쳐서
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.

# 로그인
def login(request) :
    if request.method=='POST' :
        # data는 forms.form 두번쨰 인자이므로 data = 은 생략 가능
        form = AuthenticationForm(request, data = request.POST) # 먼저 request 인자를 받아야함
        if form.is_valid() :
            # 세션 CREATE/ form.get_user는 User 객체 반환
            auth_login(request, form.get_user())
            return redirect('articles:index') # 로그인 성공시 메인페이지 이동

    else :
        form = AuthenticationForm()

    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)


# 회원가입
def signup(request) :
    if request.method== "POST" :
        form = UserCreationForm(request.POST)
        if form.is_valid() :
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else : # 회원가입 페이지 첫 접근
        form = UserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/register.html', context)


# 비밀번호
def update_password(request) :
    if request.method == "POST" :
        form =PasswordChangeForm(request.user, request.POST)
        if form.is_valid() :
            user = form.save() # 이때 로그아웃처리됨. session 정보 날라가고, 로그인정보도 사라짐
            update_session_auth_hash(request, user) # session 을 update 이렇게 해야 비밀번호를 바꾸더라도 로그아웃이 되지 않음
            return redirect('articles:index')
    else :
        form = PasswordChangeForm(request.user)
    context = {
        'form':form,
    }
    return render(request, 'accounts/password.html', context)

