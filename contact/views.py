from django.shortcuts import render, redirect
from contact.forms import ContactForm
from django.core.mail import send_mail
from django.template.loader import get_template

def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = form.cleaned_data['contact_email']
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)
            
            email = send_mail(
            "New contact form submission",
             content, 
             None, 
             ['daniel.morales117@yahoo.com'], 
             fail_silently=True)
            return redirect('contact')

    return render(request, 'contact_index.html', {'form': form_class})