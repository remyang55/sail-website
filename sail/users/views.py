from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

"""EMAIL IMPORTS"""
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from .token_generator import account_activation_token
"""EMAIL IMPORTS"""

from .models import SailTeacher, SailStudent
from .forms import (SailUserCreationForm, 
                    SailTeacherCreationForm,
                    SailStudentCreationForm,
                    SailUserUpdateForm
)

def register(request):
    return render(request, 'users/register.html')

# Credits to https://blog.hlab.tech/part-ii-how-to-sign-up-user-and-send-confirmation-email-in-django-2-1-and-python-3-6/
def _send_register_confirmation_email(request, user, to_email):
    email_subject = 'Activate your Sail Account'
    current_site = get_current_site(request)

    message = render_to_string('users/register_activate.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user)
    })

    email = EmailMessage(email_subject, message, to=[to_email])
    email.send()

def activate_account(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = get_user_model().objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Your account has been activated successfully. You may login now!')
        return redirect('users_login')
    else:
        messages.error(request, 'The activation link seems to be invalid!')
        return redirect('sail_home')

def register_teacher(request):
    if request.method == 'POST':
        u_form = SailUserCreationForm(request.POST)
        p_form = SailTeacherCreationForm(request.POST)
        if u_form.is_valid() and p_form.is_valid():
            user = u_form.save(commit=False)
            user.is_active = False
            user.save()

            teacher = p_form.save(commit=False)
            teacher.user = user
            teacher.save()

            _send_register_confirmation_email(request, user, u_form.cleaned_data['email'])

            messages.success(request, 'Account created! You will need to verify your account in your email before you can login.')
            return redirect('users_login')
    else:
        u_form = SailUserCreationForm()
        p_form = SailTeacherCreationForm()
    
    context = {'u_form':u_form, 'p_form':p_form}

    return render(request, 'users/register_form.html', context)

def register_student(request):
    if request.method == 'POST':
        u_form = SailUserCreationForm(request.POST)
        p_form = SailStudentCreationForm(request.POST)
        if u_form.is_valid() and p_form.is_valid():
            user = u_form.save(commit=False)
            user.is_active = False
            user.save()

            student = p_form.save(commit=False)
            student.user = user
            student.save()

            _send_register_confirmation_email(request, user, u_form.cleaned_data['email'])

            messages.success(request, 'Account created! You will need to verify your account in your email before you can login.')
            return redirect('users_login')
    else:
        u_form = SailUserCreationForm()
        p_form = SailStudentCreationForm()
    
    context = {'u_form':u_form, 'p_form':p_form}

    return render(request, 'users/register_form.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        if request.POST['action'] == 'Update':
            form = SailUserUpdateForm(request.POST, instance=request.user)
            if form.is_valid():
                user = form.save()
                messages.success(request, 'Account updated!')
                return redirect('users_profile')
        elif request.POST['action'] == 'Delete':
            request.user.delete()
            messages.success(request, 'Account deleted')
            return redirect('sail_home')
    else:
        form = SailUserUpdateForm(instance=request.user)
    return render(request, 'users/profile.html', {'form':form})
