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

          form.send_mail()

          messages.success(request, 'E-mail enviado com sucesso')

          form = ContatoForm()

    else:
        messages.error(request, 'Erro ao enviar e-mail')

    context = {
        'form': form
    }
    return render(request, 'contato.html', context)