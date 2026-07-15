from django.shortcuts import render, redirect , get_object_or_404
from .forms import ContactForm
from .models import Book 

def home_view(request):
    books = Book.objects.all().order_by('-created')[:6]
    return render(request, 'home.html', {'books': books})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('landing:home') 
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def book_detail_view(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_detail.html', {'book': book})