
from django.shortcuts import render

def under_construction(request):
    template_dictionary = {}
    template_dictionary['title'] = 'Digital Rain - Matrix Rain - Geek Rain'
    
    return render(request, 'under_construction.html', template_dictionary)