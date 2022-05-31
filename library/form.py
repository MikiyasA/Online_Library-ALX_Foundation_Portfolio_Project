from django import forms
from . models import *


class AuthorCreateForm(forms.ModelForm):
    """A class to create form for Author"""
    class Meta:
        model = Author
        fields = ['author_name', 'address', 'phone', 'email', 'bio']

    def clean_author_id(self):
        """The function to check if the Author ID is already exist"""
        author_id = self.cleaned_data.get('author_id')
        for instance in Author.objects.all():
            if instance.author_id == author_id:
                raise forms.ValidationError("Author ID assignment error" + author_id)
        return author_id


class ShelfCreateForm(forms.ModelForm):
    """A class to create form for Shelf"""
    class Meta:
        model = Shelf
        fields = ['location', 'category', 'cover']

    def clean_shelf_id(self):
        """The function to check if the Shelf ID is already exist"""
        shelf_id = self.cleaned_data.get('shelf_id')
        for instance in Shelf.objects.all():
            if instance.shelf_id == shelf_id:
                raise forms.ValidationError("Shelf ID assignment error" + shelf_id)
        return shelf_id


class BooksCreateForm(forms.ModelForm):
    """A class to create form for Book"""
    class Meta:
        model = Book
        fields = ['book', 'book_name', 'author', 'edition', 'type',
                  'shelf_id', 'cover', 'staff_id']

    def clean_book_id(self):
        """The function to check if the Book ID is already exist"""
        book_id = self.cleaned_data.get('book_id')
        for instance in Book.objects.all():
            if instance.book_id == book_id:
                raise forms.ValidationError("Book ID assignment error" + book_id)
        return book_id


class BlogCreateForm(forms.ModelForm):
    """A class to create form for Blog"""
    class Meta:
        model = Blog
        fields = ['title', 'description', 'photo']

