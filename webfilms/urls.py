from django.urls import path
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    path("", views.home, name="homie"),
    path("home/", views.home, name="home"),
    path("forum/", views.forum_list, name="forum_list"),
    path('delete/<post_id>',views.delete_post,name='delete'),
    path('forum/post/<int:pk>/', views.post_detail, name='post_detail'),
    path('forum/post/new', views.post_new, name='post_new'),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.logout, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("login/", views.login, name="login"),
    path("profile/remove_rating/<int:movie_rating_id>", views.remove_rating, name="remove_rating"),
    path("profile/change_rating/<int:movie_rating_id>/<int:new_rating>", views.change_rating, name="change_rating"),
    path("ratemovie/<slug:imdb_id>/<int:rating>", views.rate_movie, name="rate_movie"),
]
