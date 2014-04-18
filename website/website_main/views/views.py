from datetime import datetime
import random

from django.shortcuts import render

def home(request):
    template_dictionary = {}
    template_dictionary['right_now'] = datetime.utcnow()
    template_dictionary['pagetitle'] = 'Digital Rain - Matrix Rain - Geek Rain'
    
    
    return render(request, 'home.html', template_dictionary)
