import django
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.core.context_processors import csrf
from mails.models import LeaveMessage

from mails.forms import LeaveMessageForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect

def message(request):

    if request.method == "POST":
        msg_form = LeaveMessageForm(request.POST)
        if msg_form.is_valid():
            name    = msg_form.cleaned_data['name'],
            email   = msg_form.cleaned_data['email'],
            content = msg_form.cleaned_data['content']
            msg = LeaveMessage(name    = name,
                               email   = email,
                               content = content
            )
            msg.save()

            mail_from = "{} <{}>".format(''.join(name), ''.join(email))
            subject = "New message from {}.".format(mail_from)
            send_mail(subject, content, mail_from, settings.DEFAULT_TO_EMAIL, fail_silently=False)

    else:
        msg_form = LeaveMessageForm()

    return redirect('/')