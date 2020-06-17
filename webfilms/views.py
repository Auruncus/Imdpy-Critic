from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from webfilms.models import *
from webfilms.forms import RateMovieForm, LoginForm
from webfilms.utils import *
from django.contrib.auth import login as auth_login 
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
import json
import sys
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Avg
from django.db.models import Q
from .models import Post
from .forms import PostForm

def forum_list(request):
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        return render(request, "forum.html", {'posts': posts}) 

def delete_post(request,post_id=None):
    post_to_delete=Post.objects.get(id=post_id)
    post_to_delete.delete()
    return HttpResponseRedirect("/forum/")        

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

def post_new(request):
     if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
     else:
        form = PostForm()
     return render(request, 'post_new.html', {'form': form})

def home(request):
    
    if request.method == "POST":
        form = RateMovieForm(request.POST)
        if form.is_valid():

            title = form.cleaned_data.get('title')
            rating = form.cleaned_data.get('rating')

            ia = IMDb()
            movies = ia.search_movie(title)
            suggestions_title = []
            suggestions_year = []
            movie_ids = []
            for movie in movies:
                if movie["kind"] is "movie":
                    try:
                        MovieRating.objects.get(user = request.user, imdb_movie_id = movie.movieID)
                    except ObjectDoesNotExist:
                        try:
                            suggestions_year.append(movie["year"])
                        except:
                            suggestions_year.append(0000)
                        suggestions_title.append(movie["title"])
                        movie_ids.append(movie.movieID)
            suggestions = zip(suggestions_title, suggestions_year, movie_ids)
            return render(request, "specify.html", {"title":title,
                                                    "rating":rating,
                                                    "suggestions": suggestions})

    else:
        form = RateMovieForm()
    return render(request, "home.html", {"form":form})

def login(request):
    if request.method == 'POST':
        logout(request)
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid credentials!')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def profile(request):
    profile_list = Profile.objects.exclude(user = request.user)
    user_list = []
    for profile in profile_list:
        user_list.append(profile.user)
    rated_movies = MovieRating.objects.filter(user=request.user)
    return render(request, "profile.html", {"user_list":user_list,
                                            "movies_list":rated_movies})
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect("/home/")

def remove_rating(request, movie_rating_id):
    movie_rating = MovieRating.objects.get(id=movie_rating_id)
    movie_rating.delete()
    return HttpResponseRedirect("/profile/")

def change_rating(request, movie_rating_id, new_rating):
    movie_rating = MovieRating.objects.get(id=movie_rating_id)
    movie_rating.rating = new_rating
    movie_rating.save()
    return HttpResponseRedirect("/profile/")

def rate_movie(request, imdb_id, rating):
    ia = IMDb()
    return_message= ""
    movie = ia.get_movie(imdb_id)
    try:
        mrating = MovieRating(user = request.user, imdb_movie_id=imdb_id,
                                title = movie["title"], rating=rating)
        mrating.save()
        for director in movie["director"]:
            drating = DirectorRating(user=request.user, director = director["name"],
                                        imdb_person_id = director.personID, rating = rating)
            drating.save()
        for writer in movie["writer"]:
            wrating = WriterRating(user=request.user, writer = writer["name"],
                                    imdb_person_id = writer.personID, rating = rating)
            wrating.save()
        for index in range(6):
            actor = movie["cast"][index]
            arating = ActorRating(user=request.user, actor = actor["name"],
                                    imdb_person_id=actor.personID, rating=rating)
            arating.save()

        for genre in movie["genres"]:
            grating = GenreRating(user=request.user, genre = genre, rating = rating)

            grating.save()

    except:
        pass

    return HttpResponseRedirect("/home/")


