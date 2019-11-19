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
    question_vote = question.survey.all() #???
    if request.method=="POST":
        content_child= request.POST.get('contentchild')
        qs = Btestchild()
        qs.survey = content_child
        qs.question = question
        qs.save()
        context = {
            "question" : question,
            "question_vote" : question_vote
        }

        return render(request , 'btest/detail.html' , context)
    else:
        context= {
            "question" : question,
            "question_vote" : question_vote
        }
        return render(request, "btest/detail.html" ,context )

def vote_mod(request , btestchild_id , btest_id):
    qs  = Btestchild.objects.get(id = btestchild_id)

    ques = Btest.objects.get(id= btest_id)

    cont

    return redirect('btest:index' )

def question_del(request , btest_id):
    ques = Btest.objects.get(id=btest_id)
    ques.delete()

    return redirect('btest:index')

def vote(request , btestchild_id , btest_id):

    return redirect('btest:index')
    
