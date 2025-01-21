from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('movies/', views.movie_list, name='movie_list'),
    path('movies/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('movies/<int:movie_id>/add-to-wishlist/', views.add_to_wishlist, name='add_to_wishlist'),
    path('movies/<int:movie_id>/add-review/', views.add_review, name='add_review'),
    path('movies/<int:movie_id>/rent/', views.rent_movie, name='rent_movie'),
    path('process-payment/', views.process_payment, name='process_payment'),
    ]