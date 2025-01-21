from django.contrib import admin
from .models import Movie, Wishlist, Review, Rent

# Register your models here.
admin.site.register(Movie)
admin.site.register(Wishlist)
admin.site.register(Review)
admin.site.register(Rent)