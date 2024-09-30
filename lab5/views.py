from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "lab5/index.html")

def list_books(request):
    return render(request, 'lab5/list_books.html')

def viewbook(request, bookId):
    return render(request, 'lab5/one_book.html')

def aboutus(request):
    return render(request, 'lab5/aboutus.html')

def one_book(request):
    return render(request, 'lab5/one_book.html')