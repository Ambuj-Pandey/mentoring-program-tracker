from email import message
from unicodedata import name
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import auth
from django.http import HttpResponse
from django.contrib.auth import logout
from accounts.models import StudentProfile, User


def login(request):
    if request.method == 'POST':
        email= request.POST['email']
        password= request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user:
            auth.login(request, user)
            if request.user.is_staff:
                return redirect('/facultydashboard')
               
            else:
                return redirect('/studentdashboard')
        
        else:
            messages.info(request, "Check your cerdentials")
            return render(request, 'login-page.html')

    else: 
        return render(request, 'login-page.html')