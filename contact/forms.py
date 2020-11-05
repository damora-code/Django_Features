from django import forms

class ContactForm(forms.Form):
    contact_name = forms.CharField(
        required=True, 
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
                'placeholder' : "name here"
            }
        ))
    contact_email = forms.EmailField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
                'placeholder' : "email here"
            }
        )
        )
    content = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                'class': "form-control",
                'placeholder' : "message here"
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Your name:"
        self.fields['contact_email'].label = "Your email:"
        self.fields['content'].label = "Message:"