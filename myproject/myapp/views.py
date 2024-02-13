from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Quote, Author
from .forms import AuthorForm, QuoteForm


@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myapp:quotes')  # Припустимо, що це шлях до сторінки з цитатами
    else:
        form = AuthorForm()
    return render(request, 'myapp/add_author.html', {'form': form})


@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.save(commit=False)
            quote.save()
            return redirect('myapp:quotes')  # Перенаправлення на сторінку з усіма цитатами
    else:
        form = QuoteForm()
    return render(request, 'myapp/add_quote.html', {'form': form})


def all_quotes(request):
    quotes = Quote.objects.all()
    return render(request, 'myapp/quotes.html', {'quotes': quotes})


def author_detail(request, author_id):
    author = Author.objects.get(id=author_id)
    return render(request, 'myapp/author_detail.html', {'author': author})
