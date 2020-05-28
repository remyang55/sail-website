from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import SailTeacher, SailStudent
from .forms import (SailUserCreationForm, 
                    SailTeacherCreationForm,
                    SailStudentCreationForm,
                    SailUserUpdateForm
)

def register(request):
    return render(request, 'users/register.html')

def register_teacher(request):
    if request.method == 'POST':
        u_form = SailUserCreationForm(request.POST)
        p_form = SailTeacherCreationForm(request.POST)
        if u_form.is_valid() and p_form.is_valid():
            user = u_form.save()
            teacher = p_form.save(commit=False)
            teacher.user = user
            teacher.save()
            messages.success(request, 'Account created! You may login now.')
            return redirect('users-login')
    else:
        u_form = SailUserCreationForm()
        p_form = SailTeacherCreationForm()
    
    context = {'u_form':u_form, 'p_form':p_form}

    return render(request, 'users/register-form.html', context)

def register_student(request):
    if request.method == 'POST':
        u_form = SailUserCreationForm(request.POST)
        p_form = SailStudentCreationForm(request.POST)
        if u_form.is_valid() and p_form.is_valid():
            user = u_form.save()
            student = p_form.save(commit=False)
            student.user = user
            student.save()
            messages.success(request, 'Account created! You may login now.')
            return redirect('users-login')
    else:
        u_form = SailUserCreationForm()
        p_form = SailStudentCreationForm()
    
    context = {'u_form':u_form, 'p_form':p_form}

    return render(request, 'users/register-form.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        if request.POST['action'] == 'Update':
            form = SailUserUpdateForm(request.POST, instance=request.user)
            if form.is_valid():
                user = form.save()
                messages.success(request, 'Account updated!')
                return redirect('users-profile')
        elif request.POST['action'] == 'Delete':
            request.user.delete()
            messages.success(request, 'Account deleted')
            return redirect('sail-home')
    else:
        form = SailUserUpdateForm(instance=request.user)
    return render(request, 'users/profile.html', {'form':form})
