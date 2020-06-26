from django.apps import apps
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import get_user_model
from django.core import mail

from .forms import SendStaffEmailForm
from .models import StaffEmail

""" Menu for staff to select which staff action to perform """
@staff_member_required(login_url='users-login')
def staff_actions(request):
    return render(request, 'staff/staff_actions.html')

""" Page where staff can send email to various groups of users """
@staff_member_required(login_url='users-login')
def send_email(request):
    if request.method == 'POST':
        form = SendStaffEmailForm(request.POST)
        if form.is_valid():
            form.save()

            subject = form.cleaned_data['subject']
            msg = form.cleaned_data['content']
            send_to = form.cleaned_data['send_to']

            if send_to == StaffEmail.TEACHER:
                to_emails = get_user_model().objects.filter(is_active=True).filter(role=StaffEmail.TEACHER).values_list('email', flat=True)
            elif send_to == StaffEmail.STUDENT:
                to_emails = get_user_model().objects.filter(is_active=True).filter(role=StaffEmail.STUDENT).values_list('email', flat=True)
            elif send_to == StaffEmail.USER:
                to_emails = get_user_model().objects.filter(is_active=True).values_list('email', flat=True)
            elif send_to == StaffEmail.P_STUDENT:
                to_emails = apps.get_model('users', 'Follower').objects.filter(role=StaffEmail.P_STUDENT).values_list('email', flat=True)
            elif send_to == StaffEmail.P_TEACHER:
                to_emails = apps.get_model('users', 'Follower').objects.filter(role=StaffEmail.P_TEACHER).values_list('email', flat=True)
            elif send_to == StaffEmail.PARENT:
                to_emails = apps.get_model('users', 'Follower').objects.filter(role=StaffEmail.PARENT).values_list('email', flat=True)
            elif send_to == StaffEmail.FOLLOWER:
                to_emails = apps.get_model('users', 'Follower').objects.all().values_list('email', flat=True)

            connection = mail.get_connection()
            connection.open()
            email = mail.EmailMultiAlternatives(
                subject = subject,
                bcc = to_emails,
            )
            email.attach_alternative(msg, "text/html")  # Need to format as HTML to preserve TinyMCE content formatting
            email.send()
            connection.close()

            messages.success(request, 'Email successfully sent!')
            return redirect('staff-actions')
    else:
        form = SendStaffEmailForm()
    
    context = {'form':form, 'title':'Staff Send Email'}
    return render(request, 'staff/send_email.html', context)
