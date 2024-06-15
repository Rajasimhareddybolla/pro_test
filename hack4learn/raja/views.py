from django.shortcuts import render
# Create your views here.
from django.http import JsonResponse

def greet(request):
    return JsonResponse({'message' :"hello world from ananymous"})
def home (request):
    return render(request , 'home.html')