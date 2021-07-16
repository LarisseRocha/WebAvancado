from django.shortcuts import render

# Create your views here.
def index(request):
    testChave = {
        'curso': 'Desenvolvimento Web Avançado'
    }
    return  render(request,'index.html', testChave)