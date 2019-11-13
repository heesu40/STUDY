from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request , "utilities/index.html")
def fonts(request):
    return render(request , "utilities/fonts.html")