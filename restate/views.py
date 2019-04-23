from django.shortcuts import render,redirect
from .forms import ContactForm, AboutForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage

# Create your views here.


def home(request):
    return render(request, 'restate/home.html')


def project(request):
    if request.method == 'POST':
        form = AboutForm(request.POST)
        if form.is_valid():
            form.save()
            First_name = form.cleaned_data.get('First Name')
            Last_name = form.cleaned_data.get('Last Name')
            Phone_number = form.cleaned_data.get('Mobile Number (Preferred Whatsapp Number) ')
            Looking_for = form.cleaned_data.get('Looking For')
            AreaPreferred = form.cleaned_data.get('Area Preferred')
            Budget = form.cleaned_data.get('Budget')
            body = {'First Name':First_name,'Last Name':Last_name,'Mobile Number (Preferred Whatsapp Number)':Phone_number,'Looking For':Looking_for,'Area Preferred':AreaPreferred, 'Budget':Budget},

            email = EmailMessage(
                'Contact From',
                str(body),
                to=['pawanacharya1979@gmail.com']
            )
            email.send()
            messages.success(request, 'Thank You! for contacting us, we will get back to you soon.')
            return HttpResponseRedirect('/project/')
    else:
        form = AboutForm()
    return render(request, 'restate/about.html', {'form': form})


def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('Name')
            email = form.cleaned_data.get('Email')
            phone = form.cleaned_data.get('phone_number')
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('Message')
            body = {'Name':name,'Email':email,'phone_number':phone,'subject':subject,'Message':message},

            email = EmailMessage(
                'Contact From',
                str(body),
                to=['pawanacharya1979@gmail.com']
            )
            email.send()
            messages.success(request, 'Thank You! for contacting us, we will get back to you soon.')
            return HttpResponseRedirect('/contact/')
    else:
        form = ContactForm()
    return render(request, 'restate/contactus.html', {'form': form})


def nricorner(request):
    return render(request, 'restate/nricorner.html')


def aboutestate(request):
    return render(request, 'restate/aboutestate.html')
