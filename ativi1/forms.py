from django import forms
from django.core.mail.message import EmailMessage

class ContatoForm(forms.Form):
    name = forms.CharField(label='name')
    email = forms.EmailField(label='email')
    msg_subject = forms.CharField(label='msg_subject')
    message = forms.CharField(label='message', widget=forms.Textarea())

    def send_mail(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        msg_subject = self.cleaned_data['msg_subject']
        message = self.cleaned_data['message']

        conteudo = f'Nome:{name}\nE-mail:{email}\nAssunto:{msg_subject}\nMensagem:{message}'
        mail = EmailMessage(
            subject='E-mailenviadopelosistemaDjango',
            body=conteudo,
            from_email='contato@seudominio.com.br',
            to=['contato@seudominio.com.br', ],
            headers={'Reply.To': email},
        )
        mail.send()