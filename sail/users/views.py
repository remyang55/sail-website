from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SailUserCreationForm

def register(request):
    if request.method == 'POST':
        form = SailUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created! You may login now.')
            return redirect('sail-home')
    else:
        form = SailUserCreationForm()
    return render(request, 'users/register.html', {'form':form})
