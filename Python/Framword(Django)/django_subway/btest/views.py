from django.shortcuts import render , redirect
from .models import Btest , Btestchild

# Create your views here.
def index(request):
    content = Btest.objects.all()
    context = {
        'question_all' : content
    }
    return render(request , 'btest/index.html' , context)

def create(request):
    if request.method == "POST":
        content = request.POST.get('content')
        btest = Btest()
        btest.question = content
        btest.save()

        return redirect('btest:index')

    else:
        return render(request, "btest/create.html")

def detail(request, btest_id):
    
    question = Btest.objects.get(id=btest_id)
    #자식테이블명_set
    #부모 테이블을 가진 모든 자식 테이블을 가져 온다.
    question_vote = question.btestchild_set.all() 

   
    context= {
        "question" : question,
        "question_vote" : question_vote
    }
    return render(request, "btest/detail.html" ,context )

def survey(request, btest_id):
    q = Btest.objects.get(id=btest_id)
    text = request.POST.get('detailadd')
    ques = Btestchild()
    ques.survey = text
    ques.question = q # 부모테이블에 저장,  FK이기 때문에 필수
    ques.save()
``
    return redirect('btest:detail' , btest_id)

def survey_mod(request , btestchild_id ):
    ques = Btestchild.objects.get(id=btestchild_id)
    
    if request.method =="POST":
        
        text = request.POST.get('detailadd')
        ques.survey = text
        ques.save()

        return redirect('btest:detail' ,ques.question_id )
    else:
        context = {
            "question_vote" : ques
        }
        return render(request, 'btest/survey_mod.html' , context )
    
