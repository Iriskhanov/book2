from django.shortcuts import render, redirect
from django.views import View
from books.models import Book



def index(request):
    book = Book.objects.all()
    return render(request, 'index.html', {'books': book})

def create(request):
    if request.POST:
        name = request.POST.get('name')
        author = request.POST.get('author')
        image = request.FILES.get('image')
        book = Book(name=name, author=author, image=image)
        book.save()
        return redirect ('home')
    return render(request, 'create.html')


