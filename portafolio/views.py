from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import project
from .forms import contactForm
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.contrib import messages

def home_portafolio(request):
    projects =  project.objects.all().order_by('-created')[:6]

    contact_form = contactForm(request.POST or None)

    if request.method == 'POST' and contact_form.is_valid():
        Full_name = contact_form.cleaned_data.get('Full_name')
        email = contact_form.cleaned_data.get('email')
        contact_message = contact_form.cleaned_data.get('contact_message')

        user_email = 'procontact325@gmail.com'
        system_email = 'meve404nonreply@gmail.com' # The system's email
        email_subject = 'Contact form was submited in portafolio.'
        email_context = { 'Full_name':Full_name,  'email':email,
                           'contact_message':contact_message}
        html_message = get_template('emails/contact_email.html') #the html template
        plain_message = f'''Hi Miguel!, \n you are receiving this email because the contact form from the portafolio was submited.
                         \n Name or company: { Full_name } \n email: { email } \n Message: { contact_message }''' #plain text message

        subject, from_email, to = email_subject, system_email, user_email #asgins the subject, from and to 
        html_content = html_message.render(email_context) #gets the context and renders it to the html template
        email = EmailMultiAlternatives(subject, plain_message, from_email, [to])
        email.attach_alternative(html_content, "text/html") #the email can be html or plain text
        email.send(fail_silently=False) #sends the email True to check if the email was successfully sent
        messages.success(request, f'{Full_name}, the message was sent to Miguel, he will be replying to you as soon as posible!')
        return redirect('home-portafolio')

    context={'projects':projects, 'contact_form':contact_form}
    return render(request, 'portafolio/home_portafolio.html', context)