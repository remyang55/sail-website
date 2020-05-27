from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SailUserCreationForm

def register(request):
    if request.method == 'POST':
        form = SailUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created! You may login now.')
            return redirect('users-login')
    else:
        form = SailUserCreationForm()
    return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')
