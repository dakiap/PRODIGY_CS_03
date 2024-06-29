from django.shortcuts import render
from django.http import JsonResponse
from .utils import assess_password_strength

def index(request):
    return render(request, 'checker/index.html')

def assess(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        strength, feedback = assess_password_strength(password)
        return JsonResponse({'strength': strength, 'feedback': feedback})
