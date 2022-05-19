from django.contrib import auth, messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from sentiment_analysis.apps.authapp.forms import UserRegisterForm


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def logout(request):
    auth.logout(request)
    return redirect('auth:login')


def register(request):
    title = 'Регистрация'

    if request.method == 'POST':
        register_form = UserRegisterForm(request.POST)

        if register_form.is_valid():
            register_form.save()
            return redirect('auth:login')
    else:
        register_form = UserRegisterForm()

    content = {'title': title, 'register_form': register_form}

    return render(request, 'registration.html', content)
