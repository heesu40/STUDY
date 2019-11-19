from django.shortcuts import render , redirect
from .models import Article , Comment

# Create your views here.
def index(requests):
    # articles = Article.objects.all()
    #쿼리셋 형태로 전체 목록이 날아온다.

    #리스트 내용을 역순으로 하는 방법 1번째 파이썬에서 정렬 하는 방법
    # articles = Article.objects.all()[::-1]

    #리스트 내용을 역순으로 하는 방법 2번째 , 불러올때 정렬시키는 법
    articles = Article.objects.order_by('-id') 
    # 쿼리셋으로 리턴될때만 사용가능 , 값이 한 행만 날아오는 경우 제대로 작동하지않는다. 
    # 그래서 get의 경우 오류가 나지만 filter의 경우 오류가 안난다.

    context = {
        "articles" : articles,
    }
    return render (requests , "crud/index.html" , context)

def new(request):
    print(f'new : {request.method}')
    if request.method == 'POST':
        title = request.POST.get("title")
        content = request.POST.get("content")

        #DB에 저장시키자
        article = Article()
        
        article.title = title
        article.content = content
        article.save()
    

        return redirect('crud:index')
    else:
        return render(request , "crud/new.html")

#form 에서 데이터를 받아 DB에 저장하고 글작성 성공메세지 출력
    # def create(request):
    #     title = request.POST.get("title")
    #     content = request.POST.get("content")

    #     #DB에 저장시키자
    #     article = Article()
        
    #     article.title = title
    #     article.content = content
    #     article.save()
        

    #     return render(request, "crud/created.html")

def detail(request, art_pk):

    
    article = Article.objects.get(pk=art_pk) #앞은 table에 저장된 pk 뒤의 pk는 입력 받은 pk
    com = article.comment_set.all()
    comlen = len(com)

    #자동적으로 생기는 것은 id인데 왜 pk를 쓸수 있나?
    #id_exact = pk 로 등록이 되어있어 pk이용이 가능하다. 
    #만약 필터(filter)로 한다면 해당값은 쿼리셋으로 날아오기 떄문에 그 경우 for문을 사용해 주어야 한다.
    context = {
        "article" : article,
        "comments" : com,
        "comlen" : comlen,
    }
    return render(request, "crud/detail.html" , context)

def update(request, art_pk):
    
    if request.method == 'POST':
        article = Article.objects.get(pk=art_pk)

        title = request.POST.get("title")
        content = request.POST.get("content")

        #새로운 내용을 본 테이블의 해당 내역에 넣어준다.
        article.title = title
        article.content = content
        article.save()
        #save되면 바뀐 값이 최종으로 된다.

        return redirect('crud:detail',article.id) 
    else:
        print(f'update : {request.method}')
        article = Article.objects.get(pk=art_pk)
        context = {
            "article" : article,

        }
        return render(request , "crud/update.html" , context)

# def revise(request, pk): #pk받아오는 방법이 url에서 id 값 받아오는 것이다~
#     print(f'save : {request.method}')
#     article = Article.objects.get(pk=pk)

#     title = request.POST.get("title")
#     content = request.POST.get("content")

#     #새로운 내용을 본 테이블의 해당 내역에 넣어준다.
#     article.title = title
#     article.content = content
#     article.save()
#     #save되면 바뀐 값이 최종으로 된다.

#     return redirect('crud:detail',article.id) 

def delete(request, art_pk):
    article = Article.objects.get(pk=art_pk)
    
    if request.method == "POST":
        

        article.delete()

        return redirect('crud:index') #삭제해서 뭐 받아 올 필요도 없고 하니 바로 홈으로!
    else:
        return redirect('crud:detail' , article.id)


# 코멘트는 POST로 날아올 것이다. art_id/comment
def comment(request, art_id):
    article = Article.objects.get(id=art_id)

    if request.method == 'POST':
        comment = request.POST.get('comment')
        #comment에 해당 부분을 적용할 것이다.

        com = Comment()
        com.comment = comment
        com.article = article #부모 정보도 저장해준다.
        com.save()
    

        return redirect('crud:detail' , article.id) #art.id나 article.id나 상관없다!
        #return redirect('crud:detail',com.article_id) 이렇게 해도 된다! 
        #post일때만 저장이 될 것이다.
def comedit(request, art_id , com_id):
    com = Comment.objects.get(id=com_id) #커멘트의 id가 com_id랑 같은 것 만 가져온다.
    #간단하게 창을 만드는 것으로 해서

    if request.method =='POST':
        text =request.POST.get("comment")
        com.comment = text
        com.save()
        return redirect('crud:detail' , art_id)
    else:
        context = {
            'comment' : com

        }

        return render(request, 'crud/comedit.html' , context)
def comdel(request, art_id , com_id):
    com = Comment.objects.get(id = com_id)

    #POST형식으로 올때만 삭제를 해야하지 때문에
    if request.method == 'POST':
        com.delete()
        return redirect('crud:detail' , art_id)