from django.shortcuts import render
from main.models import *


# Create your views here.
def index(request):
    # this is the static main page
    return render(request, "main/index.html", {})
