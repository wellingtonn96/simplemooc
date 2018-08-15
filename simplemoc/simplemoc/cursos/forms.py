from django import forms
from django.core.mail import send_mail
from django.conf import settings

from simplemoc.core.mail import send_mail_template

class ContactCurso(forms.Form):

    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(
        label = 'Mensagem/Dúvida', widget=forms.Textarea
    )
 
 
 #Envio antigo, sem o uso de template
     
def send_mail(self, curso):
    subject = '[%s] Contato' % curso
    context = {
        'name': self.cleaned_data['name'],
        'email': self.cleaned_data['email'],
        'message': self.cleaned_data['message'],
    }
    template_name = 'cursos/contact_email.html'
    send_mail_template(
        subject, template_name, context, 
        [settings.CONTACT_EMAIL]
    )
