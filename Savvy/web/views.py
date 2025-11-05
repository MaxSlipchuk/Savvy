from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def login_page(request):
    return render(request, 'web/login.html')