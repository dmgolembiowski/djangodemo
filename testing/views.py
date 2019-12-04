# Create your views here.
# test.py
from django.shortcuts import render, redirect
# Create your views here.

def index(request):
    '''
    A VIEW TO CHECK IF USER IS LOGGED IN THEN REDIRECT TO CORRECT PAGE
    '''
    my_age = 14
    context_list = {
        "obj_name": "Hello Django World!!!!!!!", # <h1>{{ obj_name }}</h1>
        "obj_age": f"I am {my_age} years old.",
    }
    return render(request,'index.html', context=context_list)
