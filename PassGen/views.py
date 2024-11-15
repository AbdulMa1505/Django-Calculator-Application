from django.shortcuts import render,HttpResponse
from django.http import JsonResponse 
import random

# Create your views here.
def Home(request):
    return render (request,'home.html')
# cheacking request parameters
def PassGen(request):
    char=list('abcdefghiklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        char.extend(list('ABCDEFGHIJKLMNOPQRSTUVXYZ'))
    if request.GET.get('digits'):
        char.extend(list('1234567890'))
    if request.GET.get('symbols'):
        char.extend(list('!@#$%^&*()?/><}|'))

    length=int(request.GET.get('length',10))
    password=""
    
    password= "".join(random.choice(char) for x in range(length))
    return render(request,'password.html',{'Password':password} )
    
