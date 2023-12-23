from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .forms import UserForm


def index(request):

    context = {

    }
    return render(request, 'app/index.html', context)


def admin_page(request):

    return render(request, 'app/admin_page.html')


def login_page(request):

    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        # Redirect to admin page.
        response = redirect('/admin_page/')
        return response
    else:
        # return an 'invalid login' page message.
        message = "Invalid username or password"
        content = {
            "message": message
        }

    return render(request, 'app/login.html', content)


def register_page(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request.
        form = UserForm(request.POST)
        # Check whether it's valid
        if form.is_valid():
            # process the data in the form.cleaned_data as required

            # redirect to a new URL:
            return redirect('/admin_page/')

    else:
        form = UserForm()

    content = {
        'UserForm' : UserForm
    }

    return render(request, 'app/register.html', content)


