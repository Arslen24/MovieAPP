from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Wishlist, Review, Rent
from django.contrib import messages

def home(request):
    movies = Movie.objects.all()  # Fetch all movies from the database
    return render(request, 'rental/home.html', {'movies': movies})

def movie_list(request):
    # Fetch all movies for the dedicated movie list page
    movies = Movie.objects.all()
    return render(request, 'rental/movie_list.html', {'movies': movies})

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    reviews = Review.objects.filter(movie=movie)
    return render(request, 'rental/movie_detail.html', {'movie': movie, 'reviews': reviews})

def add_to_wishlist(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    Wishlist.objects.create(user=request.user, movie=movie)
    return redirect('wishlist')

def wishlist(request):
    user_wishlist = Wishlist.objects.filter(user=request.user)
    return render(request, 'rental/wishlist.html', {'wishlist': user_wishlist})

def add_review(request, movie_id):
    if request.method == 'POST':
        content = request.POST['content']
        rating = int(request.POST['rating'])
        movie = get_object_or_404(Movie, id=movie_id)
        Review.objects.create(user=request.user, movie=movie, content=content, rating=rating)
        return redirect('movie_detail', movie_id=movie.id)
    return render(request, 'rental/add_review.html')

def rent_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    
    # Pricing logic (static example, can be dynamic)
    rental_price = 4.99  # Example price in USD
    
    # Pass movie, pricing, and other details to the template
    context = {
        'movie': movie,
        'price': rental_price,
    }
    return render(request, 'rental/rent_confirm.html', context)

def process_payment(request):
    if request.method == 'POST':
        movie_id = request.POST.get('movie_id')
        price = request.POST.get('price')
        movie = get_object_or_404(Movie, id=movie_id)
        
        # Simulate payment processing
        Rent.objects.create(user=request.user, movie=movie)  # Record the rental
        messages.success(request, f"Payment of ${price} for {movie.title} was successful!")
        return redirect('home')
    else:
        return redirect('home')