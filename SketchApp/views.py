from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request,'index.html')

def portrait_page(request):
    return render(request,'portrait_page.html')