from django.urls import reverse
from django.contrib import auth
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def login(request):
    _next = request.GET.get('next', '/')

    if request.method == "POST":
        _next = request.POST.get('next')
        form = AuthenticationForm(request, data=request.POST)
        print('POST---:{0}'.format(request.POST))
        print('form---:{0}'.format(form))
        data =auth.login(request, form.get_user())
        print('data---:{0}'.format(data))
        if form.is_valid():
            print('---:{0}'.format("is valid"))
            auth.login(request, form.get_user())
            return HttpResponseRedirect(_next)
        print('---:{0}'.format("not valid"))
    else:
        form = AuthenticationForm(request)

    kwargs = {
        'form': form,
        'next': _next
    }

    return render(request, 'accounts/login.html', kwargs)

def test_login(request):
    _next = request.GET.get('next', '/')

    if request.method == "POST":
        _next = request.POST.get('next')
        form = AuthenticationForm(request, data=request.POST)
        print('---:{0}'.format(request.POST))
        print('---:{0}'.format(form))
        if form.is_valid():
            print('---:{0}'.format("is valid"))
            auth.login(request, form.get_user())
            return HttpResponseRedirect(_next)
        print('---:{0}'.format("not valid"))
    else:
        form = AuthenticationForm(request)

    kwargs = {
        'form': form,
        'next': _next
    }

    return render(request, 'accounts/login.html', kwargs)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('login-url'))
