from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def register(request):
    return HttpResponse("<h2>Test Register</h2>")

def login(request):
    return HttpResponse("<h2>Test Login</h2>")