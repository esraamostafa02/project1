from django.db import models

# Create your models here.
from django.conf import settings

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    total_copies = models.PositiveIntegerField(default=1)
    available_copies = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title


class Borrowing(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    book = models.ForeignKey(
        "Book",
        on_delete=models.CASCADE
    )

    borrowing_date = models.DateField()
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)

    status = models.CharField(
        max_length=20,
        default="Borrowed"
    )

    def __str__(self):
        return f"{self.user} - {self.book}"    


class Reservation(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    book = models.ForeignKey(
        "Book",
        on_delete=models.CASCADE
    )

    reservation_date = models.DateField(auto_now_add=True)

    status = models.CharField(
        max_length=20,
        default="Pending"
    )

    def __str__(self):
        return f"{self.user} - {self.book}"    