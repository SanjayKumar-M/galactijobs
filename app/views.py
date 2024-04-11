from django.shortcuts import render

def sample(request):
    return render(request, "app/sample.html")