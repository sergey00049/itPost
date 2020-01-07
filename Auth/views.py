from django.shortcuts import render, redirect
from .forms import UserOurRegistration

def register(request):
    if request.method == "POST":
         form = UserOurRegistration(request.POST)
         if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserOurRegistration()
    return render(request, 'Auth/registration.html', {'form': form, 'title': 'Регистрация'})