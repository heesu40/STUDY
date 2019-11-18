from django.shortcuts import render , redirect
from subway.models import Subway



# Create your views here.
def index(request):
    sb = Subway.objects.all()
    context = {
        "sb" : sb
    }
    return render(request , "subway/index.html" , context)

def menu(request):
    if request.method == "POST":
        name = request.POST.get('name')
        print(name)
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        bread = request.POST.get('bread')
        sauce = request.POST.get('sauce')
        vegetable = request.POST.getlist('vegetable')
        drink = request.POST.get('drink')

        sb  = Subway()
        sb.name = name
        sb.address = address
        sb.phone = phone
        sb.bread = bread
        sb.vegetable = vegetable
        sb.sauce = sauce
        sb.drink = drink
        sb.save()

        print("완료")
        

        return redirect("subway:index")
    else :

        return render(request , "subway/menu.html")

def detail(request,id):
    sb =Subway.objects.get(id=id)
    context = {
        'sb' : sb
    }
    return render(request , "subway/detail.html" , context )

def mod(request, id):
    sb = Subway.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        bread = request.POST.get('bread')
        sauce = request.POST.get('sauce')
        vegetable = request.POST.getlist('vegetable')
        drink = request.POST.get('drink')

        sb  = Subway()
        sb.name = name
        sb.address = address
        sb.phone = phone
        sb.bread = bread
        sb.vegetable = vegetable
        sb.sauce = sauce
        sb.drink = drink
        sb.save()

        return redirect('subway:detail' , sb.id)
    else:
        
        return render(request , 'subway/mod.html', sb.id)

def delete(request , id):
    sb = Subway.objects.get(id=id)
    if request.method  == 'POST':
        

        sb.delete()
        return redirect('subway:index.html')
    else:
        return redirect('subway:detail' , sb.id)


