from django.shortcuts import render, redirect
from django.contrib import messages
from . form import *
from django.db.models import Q


def home(request):
    title = 'Home'
    queryset = Blog.objects.order_by('-post_date')[:10]
    bkQueryset = Book.objects.order_by('-upload_date')[:5]
    context = {
        'title': title,
        'queryset': queryset,
        'bkQueryset': bkQueryset,
    }
    return render(request, "home.html", context)


def post_blog(request):
    title = "Post Blog"
    form = BlogCreateForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, "Author successfully added")
        return redirect('/')
    context = {
        'title': title,
        'form': form
    }
    return render(request, "add.html", context)


def shelf(request):
    title = 'Book Shelves'
    if 'q' in request.GET:
        q = request.GET['q']
        mul_q = Q(Q(shelf_id__icontains=q) | Q(location__icontains=q) | Q(category__icontains=q))
        queryset = Shelf.objects.filter(mul_q).distinct()
    else:
        queryset = Shelf.objects.all()

    context = {
        'title': title,
        'queryset': queryset,
    }
    return render(request, "shelf.html", context)


def book(request, pk):
    title = 'Book Shelves'

    if 'q' in request.GET:
        q = request.GET['q']
        mul_q = Q(Q(book_id__icontains=q) | Q(book_name__icontains=q)
                  | Q(edition__icontains=q) | Q(type__icontains=q) | Q(location__icontains=q)
                  )
        queryset = Book.objects.filter(shelf_id=pk).filter(mul_q).distinct()
    else:
        queryset = Book.objects.filter(shelf_id=pk)
    context = {
        'title': title,
        'queryset': queryset,
    }
    return render(request, "book.html", context)


def add_author(request):
    title = 'Add Author'
    form = AuthorCreateForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, "Author successfully added")
        return redirect('/shelf')
    context = {
        'title': title,
        'form': form,
    }
    return render(request, "add.html", context)


def add_shelf(request):
    title = 'Add Shelf'
    form = ShelfCreateForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, "Shelf successfully added")
        return redirect('/shelf')
    context = {
        'title': title,
        'form': form,
    }
    return render(request, "add.html", context)


def update_shelf(request, pk):
    title = 'Update Shelf'
    queryset = Shelf.objects.get(shelf_id=pk)
    form = ShelfCreateForm(instance=queryset)
    if request.method == 'POST':
        form = ShelfCreateForm(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
            print("sucess")
            messages.success(request, "Shelf successfully updated")
            return redirect('/shelf')
    context = {
        'title': title,
        'form': form,
    }
    return render(request, "add.html", context)


def add_book(request):
    title = 'Add Book'
    form = BooksCreateForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, "Book successfully added")
        return redirect('/shelf')
    context = {
        'title': title,
        'form': form,
    }
    return render(request, "add.html", context)


def update_book(request, pk):
    title = 'Update Book'
    queryset = Book.objects.get(book_id=pk)
    form = BooksCreateForm(instance=queryset)
    if request.method == 'POST':
        form = BooksCreateForm(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, "Book successfully updated")
            return redirect('/shelf')
    context = {
        'title': title,
        'form': form,
    }
    print(pk)
    return render(request, "add.html", context)


def about(request):
    title = "About"
    context = {
        'title': title,
    }
    return render(request, "about.html", context)


def contact(request):
    title = "Contacts"
    context = {
        'title': title,
    }
    return render(request, "contact.html", context)