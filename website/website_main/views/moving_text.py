
from django.shortcuts import render

def moving_text(request):
    return render(request, 'moving_text.html', {})