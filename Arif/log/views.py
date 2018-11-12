from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import Reg




def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return render(request, 'thankyou.html')
        else:
            return HttpResponse("Username or password incorrect")
    return render(request, 'login.html')




def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login')



def home(request):
   return render(request, 'home.html')




def user_signup(request):
    form = Reg(request.POST or None)
    if form.is_valid():
        isinstance=form.save(commit=False)
        isinstance.save()
        return HttpResponseRedirect('/login')
    return render(request, 'signup.html',{'signup_form':form})