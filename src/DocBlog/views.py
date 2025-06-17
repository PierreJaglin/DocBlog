from django.http import HttpResponse
from django.shortcuts import render

from datetime import datetime  

# Create your views here.

def index(request):

    date = datetime.now()

    return render(request, 'DocBlog/index.html', context={
        'prenom': 'Pierre',
        'date': date,
    })