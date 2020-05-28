from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from .models import SailParticipant
from .forms import SailUserCreationForm, SailUserUpdateForm

def register(request):
    if request.method == 'POST':
        form = SailUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # participant = SailParticipant.objects.create(user=user,
            #                                              role=form.cleaned_data['role'],
            #                                              year_in_school=form.cleaned_data['year_in_school'])
            messages.success(request, 'Account created! You may login now.')
            return redirect('users-login')
    else:
        form = SailUserCreationForm()
    return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = SailUserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account updated!')
            return redirect('users-profile')
    else:
        form = SailUserUpdateForm(instance=request.user)
    return render(request, 'users/profile.html', {'form':form})
