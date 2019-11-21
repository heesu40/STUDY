from django.shortcuts import render, redirect
from .models import Board

# Create your views here.
def index(request):
    boards = Board.objects.all()
    context= {
        "boards" : boards
    }
    return render(request, 'boards/index.html' ,context)
def new(request):
    if request.method=="POST":
        title = request.POST.get('title')
        content = request.POST.get("content")
        image = request.FILES.get('image')

        board = Board(title = title , content= content , image = image)
        board.save()

        return redirect('boards:index')
    else:
        return render(request, "boards/new.html")

def detail(request , b_id):
    board=Board.objects.get(id=b_id)
    context = {
        'board' : board
    }
    return render(request , "boards/detail.html" , context)

def edit(request, b_id):
    board = Board.objects.get(id=b_id)

    if request.method=="POST":
      
        board.title = request.POST.get('title')
        board.content = request.POST.get('content')
        img = request.FILES.get('image')
        print(img)
        if img is not None: 
            board.image = img 
        board.save()

        return redirect('boards:detail' , b_id)

    else:
       
        context = {
            'board' : board
        }
        return render(request , 'boards/edit.html' , context)