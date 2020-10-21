from django.shortcuts import render
from contact.forms import ContactForm

def contact(request):
    form_class = ContactForm

    return render(request, 'contact_index.html', {
        'form': form_class,
    })