from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import get_user_model
from django.core import mail

from .forms import SendEmailForm
from .models import Email

@staff_member_required(login_url='users_login')
def staff_actions(request):
    return render(request, 'staff/staff_actions.html')

@staff_member_required(login_url='users_login')
def send_email(request):
    if request.method == 'POST':
        form = SendEmailForm(request.POST)
        if form.is_valid():
            form.save()

            # send email
            subject = form.cleaned_data['subject']
            msg = form.cleaned_data['content']
            send_to = form.cleaned_data['send_to']

            if send_to == Email.TEACHER:
                to_emails = get_user_model().objects.filter(is_active=True).filter(role=Email.TEACHER).values_list('email', flat=True)
            elif send_to == Email.STUDENT:
                to_emails = get_user_model().objects.filter(is_active=True).filter(role=Email.STUDENT).values_list('email', flat=True)
            elif send_to == Email.USER:
                to_emails = get_user_model().objects.filter(is_active=True).values_list('email', flat=True)

            connection = mail.get_connection()
            connection.open()
            email = mail.EmailMultiAlternatives(
                subject = subject,
                bcc = to_emails,
            )
            email.attach_alternative(msg, "text/html")
            email.send()
            connection.close()

            messages.success(request, 'Email successfully sent!')
            return redirect('staff_actions')
    else:
        form = SendEmailForm()
    
    context = {'form':form, 'title':'Staff Send Email'}
    return render(request, 'staff/send_email.html', context)
