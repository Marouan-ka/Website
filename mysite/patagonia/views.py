
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import portfolo
from mysite.forms import contactform
from django.core.mail import EmailMessage

def index(request):
    portfolios = portfolo.objects.all()
    context = {'portfolios' :portfolios}
    return render(request, 'patagonia/index.html', context)

def work(request):
    zorks = portfolo.objects.all()
    context = {'zorks' :zorks}
    return render(request, 'patagonia/portfolio.html', context)

def contact(request):
    if request.method == 'POST':
        form = contactform(request.POST)
        if form.is_valid():
            # Process the form data here if needed
            if form.is_valid():
    # Access cleaned form data
                full_name = form.cleaned_data['full_name']
                email = form.cleaned_data['email']
                current_website = form.cleaned_data['current_website']
                business_do = form.cleaned_data['business_do']

                subject = 'Contact form submission from {}'.format(full_name)
                message = f"Business Do: {business_do}\nCurrent Website: {current_website}"
                from_email = email
                recipient_list = ['marouan.kaboul@gmail.com']
                reply_to = [email]

                email_message = EmailMessage(subject, message, from_email, recipient_list, reply_to)
                
                # Use send() method on the EmailMessage instance, not on recipient_list
                email_message.send()

            success_message = "Form submitted successfully!"
            messages.success(request, success_message)
            # return redirect('success')
    else:
        form = contactform()


    return render(request, 'patagonia/contact.html', {'form': form})



def portfoliopage(request, slug):
        postl = portfolo.objects.get(slug=slug)
        context = {'p': postl}
        return render(request, 'patagonia/portfoliopage.html', context)

        