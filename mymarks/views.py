from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from mymarks.models import mark, UserMeta
from django.contrib import messages


subjects = ['Математика', 'Русский', 'Химия']


def main(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/authed')
        return render(request, 'main.html')


def loginp(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/authed')
        else:
            return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('login', '')
        password = request.POST.get('password', '')

        if username == '' or password == '':
            messages.error(request, 'Заполните все поля')
            return redirect('/login')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/authed')
        else:
            messages.error(request, 'Неправильный логин или пароль!')
            return redirect('/login')


def registerp(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/authed')
        else:
            return render(request, 'register.html')
    if request.method == 'POST':
        name = request.POST.get('name', '')
        username = request.POST.get('login', '')
        email = request.POST.get('email', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')

        if username == '' or password1 == '' or password2 == '':
            messages.error(request, 'Не все поля заполнены')
            return redirect('/register')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Ник уже занят')
            return redirect('/register')
        elif len(username) < 3:
            messages.error(request, 'Слишком короткий ник')
            return redirect('/register')
        elif len(username) > 20:
            messages.error(request, 'Слишком длинный ник')
            return redirect('/register')
        elif len(password1) < 6:
            messages.error(request, 'Слишком короткий пароль')
            return redirect('/register')
        elif len(password1) > 50:
            messages.error(request, 'Слишком длинный пароль')
            return redirect('/register')
        elif password1 != password2:
            messages.error(request, 'Пароли не совпадают')
            return redirect('/register')
        else:
            user = User.objects.create_user(
                username=username, email=email, password=password1, first_name=name)
            user.save()
            login(request, user)
            return redirect('/authed')


def authed(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            user = request.user.username
            marks = mark.objects.filter(author=request.user)

            parms = {'username': request.user.username,
                     'user': request.user.first_name, 'marks': marks}
            return render(request, 'authed.html', parms)
    else:
        return redirect('/')


def logoutp(request):
    if request.method == 'GET':
        logout(request)
    return redirect('/')


def addmark(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            return render(request, 'addmark.html')
        if request.method == 'POST':
            sub = request.POST.get('subject', '')
            mar = request.POST.get('mark', '')
            des = request.POST.get('description', '')

            Mark = mark()
            Mark.author = request.user
            Mark.subject = sub
            Mark.value = mar
            Mark.description = des
            Mark.save()
            return redirect('/')
    else:
        return redirect('/')


def profilep(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            parms = {'username': request.user.username, 'user': request.user.first_name,
                     "last_name": request.user.last_name, "email": request.user.email, "last_login": request.user.last_login}
            return render(request, 'profile.html', parms)
        elif request.method == 'POST':
            if 'pdatasubm' in request.POST:
                LastName = request.POST.get('LastName', '')
                FirstName = request.POST.get('FirstName', '')
                username = request.POST.get('username', '')
                email = request.POST.get('email', '')

                user = request.user
                user.first_name = FirstName
                user.last_name = LastName
                user.email = email
                user.username = username
                user.save()

            return redirect('/authed/profile/')
    else:
        return redirect('/')


def subjectsp(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            is_first = bool(UserMeta.objects.filter(user=request.user))
            parms = {'username': request.user.username,
                     'user': request.user.first_name, 'is_first': is_first}
            return render(request, 'subjects.html', parms)
    else:
        return redirect('/')


def subjfirstsetp(request):
    global subjects
    if request.user.is_authenticated:
        if request.method == 'GET':
            step = bool(int(request.GET.get('step')))
            params = {'username': request.user.username,
                      'user': request.user.first_name, 'step': step, 'subjects': subjects}
            if step:
                d = {}
                for s in subjects:
                    d[s] = request.GET.get(s)
                params['subjects'] = d
            return render(request, 'subjectsfirst.html', params)
        elif request.method == 'POST':
            step = bool(int(request.GET.get('step')))
            if not step:
                vars = '?'
                for s in subjects:
                    vars = vars + s + '=' + request.POST.get(s, '') + '&'
                return redirect('/authed/profile/subjects/firstset' + vars + 'step=1')
            elif step:
                pass
    else:
        return redirect('/')
