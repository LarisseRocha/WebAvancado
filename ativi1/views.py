from django.shortcuts import render
from .forms import ContatoForm
from django.contrib import messages
# Create your views here.
def index(request):
    testChave = {
        'curso': 'Desenvolvimento Web Avançado'
    }
    return  render(request,'index.html', testChave)


def contato(request):
    form = ContatoForm(request.POST or None)
    if str(request.method) == 'POST':

       if form.is_valid():

         name = form.cleaned_data['name']
         email = form.cleaned_data['email']
         msg_subject = form.cleaned_data['msg_subject']
         message = form.cleaned_data['message']

         print('Mensagem Enviada')
         messages.success(request, 'E-mail enviado com sucesso')
         print(f'Nome: {name}')
         print(f'E-mail: {email}')
         print(f'Assunto: {msg_subject}')
         print(f'Mensagem: {message}')
         form = ContatoForm()

    else:

        messages.error(request, 'Erro ao enviar e-mail')

    context = {
        'form': form
    }
    return render(request, 'contato.html', context)