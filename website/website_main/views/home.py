
from django.shortcuts import render
from django.conf.urls import url
from django.conf.urls import patterns

def home(request):
    template_dictionary = {}
    template_dictionary['title'] = 'Digital Rain - Matrix Rain - Geek Rain'
    
    return render(request, 'home.html', template_dictionary)