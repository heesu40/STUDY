from django.shortcuts import render , redirect , get_object_or_404
from .forms import BoardForm , CommentForm
from .models import Board , Comment
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

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
    comment_form = CommentForm()# 댓글 보내기

    comments = board.comment_set.all()   #board에서는 역참고 할때는 _set을 붙여야 한다. 그래서 모든 값을 가져온다.
                                        # 자식입장에서는 부모가 누구인지 명확하기에 comment.board하면 부모를 불러올수 있다.


    context = {
        'board'  : board,
        'comment_form' : comment_form,
        'comments' : comments,
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
@login_required
@require_POST #POST로 왔을때만 이 함수 사용 가능!
def new_comment(request, b_id):
    form = CommentForm(request.POST) #CommentForm에 request.POST내용이 들어 가게 된다.

    if form.is_valid(): #댓글이 200자 안으로 잘쓰였는지 확인!
        comment = form.save(commit=False) #DB바로 저장을 막는다!
        comment.board_id = b_id
        comment.user =request.user #현재 페이지를 작성하는 유저, 현재 접속한 user를 불러온다.
        comment.save()
        return redirect('boards:detail', b_id)
    else:
        board = Board.objects.get(id=b_id)
        comments = board.comment_set.all()
        context = {
            'board' : board,
            'comment_form' : form,
            'comments' : comments,
        }
        return render(request, 'boards/detail.html' , context)
@login_required
@require_POST
def del_comment(request, c_id):
    comment = get_object_or_404(Comment, id=c_id)
    board_id = comment.board_id #부모의 아이디를 지우기 전에 변수에 저장
    if request.user == comment.user:
        comment.delete()
    
    return redirect('boards:detail' , board_id)

@login_required
def like(request, b_id):
    board = get_object_or_404(Board,pk=b_id)
    #좋아요는 누르면 좋아요, 다시 누르면 좋아요 취소
    #좋아요 흔적이 중계모델이 남게 된다. 이를 이용해서 좋아요 로직을 구현하게 된다.
    #중계모델에서 사용자와 게시글 두개를 동시에 가지고 있기 때문에 가능하게 된다.

    # if board.like_users.filter(id=request.user.id).exists():    #get으로 찾았을떄 없으면 에러 뜨기 때문에 filter로!
    if request.user in board.like_users.all(): #위아래 둘 중 하나를 사용하자.
        board.like_users.remove(request.user)
    else:
        board.like_users.add(request.user)
    return redirect('boards:index')
