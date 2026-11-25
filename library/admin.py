from django.contrib import admin
from .models import Book, Borrowing, Reservation

admin.site.register(Book)
admin.site.register(Borrowing)
admin.site.register(Reservation)