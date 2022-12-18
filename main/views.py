from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from email.message import EmailMessage
from django.conf import settings
from django.http import HttpResponse
# Create your views here.
from .models import *
def index(request):
    return render(request, "main/index.html")