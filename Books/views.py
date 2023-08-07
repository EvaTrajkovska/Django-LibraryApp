from django.shortcuts import render
from .models import Book
from .forms import BookForm
# Create your views here.


def books(request):
    context = {"books": Book.objects.filter(user=request.user).all(), "forms": BookForm}
    return render(request, "books.html", context=context)

