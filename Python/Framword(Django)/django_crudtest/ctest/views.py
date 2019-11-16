from django.shortcuts import render , redirect
from .models import ctest

# Create your views here.
def index(request):
    art = ctest.objects.all()

    context = {
        "art" : art
    }

    return render(request , "ctest/index.html" , context)

def addart(request):
    return render(request , 'ctest/addart.html')

def upart(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    art = ctest()
    art.title =title
    art.content = content
    art.save()
 
    return redirect('/ctest/')

def artcon(request , pk):
    art = ctest.objects.get(pk=pk)
    title = art.title
    content = art.content
    
    context ={
        "title" : title,
        "content" : content,
        "art" : art
    }
    return render(request , 'ctest/artcon.html' , context)

def artmod(request , pk):
    art=ctest.objects.get(pk=pk)
    context = {
        "art" : art
    }
    return render(request , 'ctest/artmod.html' , context)

def artdel(request , pk):
    art = ctest.objects.get(pk=pk)

    art.delete()

    return redirect ('/ctest/')

def artmod2(request, pk):
    art = ctest.objects.get(pk=pk)

    title = request.POST.get("title")
    content = request.POST.get("content")

    art.title = title
    art.content = content
    art.save()

    return redirect(f'/ctest/{art.id}/artcon/')