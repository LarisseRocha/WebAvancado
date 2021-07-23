from django import forms


class ContatoForm(forms.Form):
    name = forms.CharField(label='name')
    email = forms.EmailField(label='email')
    msg_subject = forms.CharField(label='assunto')
    message = forms.CharField(label='message', widget=forms.Textarea())
