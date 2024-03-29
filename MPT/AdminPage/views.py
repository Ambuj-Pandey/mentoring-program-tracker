from audioop import reverse
import genericpath
from typing import Generic
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from django.contrib.auth.forms import UserChangeForm
from accounts.models import StudentProfile,User
# from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def Adminpage(request):
    if request.user.is_superuser:
        user = User.objects.all()
        context = {'user': user} 
        return render(request,'AdminPage/admin-user.html',context)
    else:
        return HttpResponse("You are not authorized to view this page")

@login_required
def student(request, pk):
    user = User.objects.get(usr_id=pk)
    student=StudentProfile.objects.get(user=user)
    context = {'student' : student}
    return render(request, 'student-dashboard.html', context)



# def stud_prof(request):
#     return render(request, 'student-profile.html')
