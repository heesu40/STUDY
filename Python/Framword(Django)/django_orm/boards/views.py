from django.shortcuts import render 
from .models import Subway
from  requests  import get,post

# Create your views here.
def index(request):
    return render (request, 'boards/index.html')
def subway(request):
    return render (request , 'boards/subway.html')
def subwayresult(request):
    
    title = request.POST.get('name')
    print(title)
    nowdate = request.POST.get('date')
    sandwitch = request.POST.get('sandwitch')
    size = request.POST.get('size')
    bread = request.POST.get('bread')
    source = request.POST.get('source')



    subway = Subway()


    subway.title = title 
    subway.nowdate = nowdate 
    subway.sandwitch = sandwitch
    subway.size = size
    subway.bread = bread
    subway.source = source
    subway.save()

    sb = Subway.objects.all()
    ss = len(sb)
    result = str(sb[ss-1])
    re = result.split(",")
    

    content = {
        'name' : re[0],
        'nowdate' :re[1],
        'sandwitch' :re[2],
        'size' : re[3],
        'bread' : re[4],
        'source' : re[5],
        'sb' : sb

    }

    
    return render (request , 'boards/subwayresult.html', content)
def subwayid(request , id):
    sub = Subway.objects.get(pk = id) #혹은 id=id
    context = {
        "result" : sub,
    }
    return render(request , 'boards/subid.html' , context)
