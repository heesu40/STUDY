from django.shortcuts import render , redirect
from .models import Movie

# Create your views here.
def index(request):
    return render(request , 'movie/index.html'),
    
def movies(request):
    movie = Movie.objects.all()
    context = {
        'movie' : movie
    }
    return render(request , 'movie/movies.html' , context)

def mtitle(request , m_id):
    movie = Movie.objects.get(id=m_id)
    context = {
        'movie' : movie
    }
    return render(request , 'movie/mtitle.html' ,context)

def new(request):
    if request.method == "POST":
        title = request.POST.get("title")
        title_en = request.POST.get('title_en')
        audience = request.POST.get('audience')
        open_date = request.POST.get('open_date')
        genre = request.POST.get('genre')
        watch_grade = request.POST.get('watch_grade')
        score = request.POST.get('score')
        poster_url = request.POST.get('poster_url')
        description = request.POST.get('description')

        movie = Movie()
        movie.title=title
        movie.title_en = title_en
        movie.audience = audience
        movie.open_date = open_date
        movie.genre = genre
        movie.watch_grade = watch_grade
        movie.score = score
        movie.poster_url = poster_url
        movie.description = description
        movie.save()

        return redirect('movie:movies')
    else:
        return render(request , 'movie/new.html')

def edit(request,m_id):
    movie = Movie.objects.get(id=m_id)
    if request.method=="POST":
        title = request.POST.get("title")
        title_en = request.POST.get('title_en')
        audience = request.POST.get('audience')
        open_date = request.POST.get('open_date')
        genre = request.POST.get('genre')
        watch_grade = request.POST.get('watch_grade')
        score = request.POST.get('score')
        poster_url = request.POST.get('poster_url')
        description = request.POST.get('description')

        mm = Movie()
        mm.title=title
        mm.title_en = title_en
        mm.audience = audience
        mm.open_date = open_date
        mm.genre = genre
        mm.watch_grade = watch_grade
        mm.score = score
        mm.poster_url = poster_url
        mm.description = description
        mm.save()
        
    
        return redirect('movie:moviesdetail' , m_id)
    else:
        context = {
            'movie' : movie
        }
        return render(request , "movie/edit.html" , context)
def delete(request,m_id):
    movie = Movie.objects.get(id=m_id)
    movie.delete()

    return redirect("movie:movies")

