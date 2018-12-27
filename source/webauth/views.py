from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponseRedirect


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        next = request.POST.get('next')
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {
                'username': username,
                'password': password,
                'next': next,
                'has_error': True
            }
            return render(request, 'login.html', context=context)
        else:
            login(request, user=user)
            redirect_url = next
            if not redirect_url:
                redirect_url = reverse('webapp:order_list')
            return HttpResponseRedirect(redirect_url)

    return render(request, 'login.html', context={'next': request.GET.get('next')})


def logout_view(request):
    logout(request)
    return redirect('webauth:login')
