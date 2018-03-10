from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, logout, update_session_auth_hash, login
from django.contrib.auth.models import User, Group


# redirects to homepage
def base(request):
    response = HttpResponseRedirect('/index/')
    return response


# homepage
def index(request):
    username = request.session.get('username')
    return render(request, 'index.html',
        {"username": username}
    )


# User Registartion
def user_registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password == password1:
            if username and email and password:
                user = User.objects.create_user(username, email,  password)
                user.is_staff = True

                user.save()
                return HttpResponseRedirect('/login/')
            else:
                return HttpResponseRedirect('/registration/')
        else:
            return HttpResponseRedirect('/registration/')
    elif request.method == 'GET':
        return render(request, 'registration.html', {
            })


# User login
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # import ipdb; ipdb.set_trace()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                request.session['username'] = username
                # response = HTTPResponse()
                response = HttpResponseRedirect('/dashboard/')
                response.set_cookie('zembedkey', 'zembedvalue')
                return response
            else:
                return HttpResponseRedirect('/login/')
                # Return 'Account is not active'
                # Return a 'disabled account' error message
        else:
            return HttpResponseRedirect('/login/')
            # Return 'invalid login'
            # Return an 'invalid login' error message.
    elif request.method == "GET":
        return render(request, 'login.html', {
        })


def dashboard(request):
    username = request.session.get('username')
    return render(request, 'user_dashboard.html',
                  {"username": username}
                  )


# logout
def user_logout(request):
    try:
        del request.session['username']
        logout(request)
    except KeyError:
        pass
    return HttpResponseRedirect('/login/')
