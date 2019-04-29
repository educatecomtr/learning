from learning.forms import Contact
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail


def contact_form(request):

    if request.method == "POST":
        form = Contact(request.POST)
        if form.is_valid():

            subject = form.cleaned_data['name']
            message = form.cleaned_data['content']
            sender = form.cleaned_data['email']

            recipients = ['info@example.com']

            send_mail(subject, message, sender, recipients)

            return HttpResponseRedirect('/')
    else:
        form = Contact()

    return render(request=request, template_name='learning/contact/form.html', context={'form': form})
