from django.shortcuts import render , redirect , get_object_or_404
from .forms import BoardForm
from .models import Board
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    boards = Board.objects.all()

    context = {
        'boards' : boards
    }
    return render(request , "boards/index.html" , context)
@login_required
def new(request):
    #로그인 한사람만 글쓰기 가능!
    # if not request.user.is_authenticated:
    #     return redirect('boards:index')
    #또 다른 방법은 데코레이터! from django.contrib.auth.decorators import login_required 선언 후에


    if request.method == "POST":
        form = BoardForm(request.POST) #reqeust.POST로 오는 내용이 BoardForm에 담겨 변수에 저장
        if form.is_valid(): #넘어오는 값이 제대로된 값인지 유효성 검사를 해주는것이 is_vaild()
            board = form.save(commit=False) #로 저장해 주면 된다.알아서 폼에서 Board라는 데이터베이스 안에 저장해준다.
            board.user=request.user
            board.save()
            return redirect ('boards:index')
    else:
            
        #form.py를 사용할 것이다.
        form = BoardForm()  #form 변수에 BoardForm 불러왔다.

    #data if, else공통 부분
    context= {
        'form' : form
    }

    return render(request, "boards/new.html" , context)

def detail(request , b_id):
    board = get_object_or_404(Board, id=b_id) #get 하면 object 하고 못받으면 에러 띄우기이며 (조건작성) 해준다.

    context = {
        'board'  : board
    }
    return render(request, 'boards/detail.html' , context)

def edit(request , b_id):
    board = get_object_or_404(Board, id=b_id)

    if request.user != board.user:
        return redirect('boards:index')


    if request.method =="POST":
        form = BoardForm(request.POST , instance=board) #수정해야 하기 떄문에 instance도 넣어준다.
        if form.is_valid():
            board = form.save()
            return redirect('boards:detail' , board.id) #만약 유효성이 안됐따면 밑에 context로 가게 된다.
    else:

        form = BoardForm(instance=board)#board에 있는 값이 채워져서 넘어갈 수 있다. 

    #공통 부분
    context = {
        'form' : form
    }

    return render(request , 'boards/edit.html' , context)

def delete(request , b_id):

    board = get_object_or_404(Board , id=b_id)

    if request.user != board.user:
        return redirect('boards:index')
    
    if request.method=="POST":
        board.delete()
        return redirect("boards:index")
    return redirect("boards:detail" , board.id) #삭제 버튼 눌러도 POST아니면 그 페이지에 남아있을 것이다.
