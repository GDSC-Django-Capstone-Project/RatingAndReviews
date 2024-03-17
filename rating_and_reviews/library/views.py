from django.shortcuts import render, redirect
from .models import Book, Review
from .forms import ReviewForm

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    reviews = Review.objects.filter(book=book)
    form = ReviewForm()
    return render(request, 'library/book_detail.html', {'book': book, 'reviews': reviews, 'form': form})

def add_review(request, book_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            book = Book.objects.get(id=book_id)
            review = form.save(commit=False)
            review.book = book
            review.student = request.user
            review.save()
            return redirect('book_detail', book_id=book_id)
    return redirect('book_detail', book_id=book_id)
