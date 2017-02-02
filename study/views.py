from django.shortcuts import render
from .models import Level



# Create your views here.
def level_list(request):
    return render(request, 'edujap/level_list.html', {})