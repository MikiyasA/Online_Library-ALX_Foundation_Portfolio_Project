import datetime

from django.db import models


def author_idno():
    """To generate auto increment book ID """

    prfx = "AUT"  # prefix of the ID
    last = Author.objects.all().last()
    if not last:
        aut_id = "{}{}".format(prfx, '0001')
        return aut_id
    last = str(last)
    last = last.replace(' - AUT', ', ')
    last = last.split(', ')
    last = last[1]
    last = int(last)
    aut_id = "{}{:04d}".format(prfx, (last + 1))
    return aut_id


class Author(models.Model):
    """ class of Author to define entities """
    author_id = models.CharField(max_length=45, blank=False, unique=True, editable=False, default=author_idno)
    author_name = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=1000, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    bio = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return "{} - {}".format(self.author_name, self.author_id)


def shelf_idno():
    """To generate auto increment book ID """
    prfx = "SLF"  # prefix of the ID
    last = Shelf.objects.all().last()
    if not last:
        slf_id = "{}{}".format(prfx, '0001')
        return slf_id
    last = str(last)
    last = last.replace('SLF', ', ')
    last = last.split(', ')
    last = last[1]
    last = int(last)
    slf_id = "{}{:04d}".format(prfx, (last + 1))
    return slf_id


class Shelf(models.Model):
    """ class of Shelf to define entities """
    shelf_id = models.CharField(max_length=45, blank=False, unique=True, editable=False, default=shelf_idno)
    location = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=100, blank=False, null=True)
    no_of_books = models.IntegerField(blank=True, null=True)
    cover = models.ImageField(upload_to='media', blank=True, default='media/def_shelf.jpg')

    def __str__(self):
        return "{}".format(self.shelf_id)


sex_choices = {
    ('Male', 'Male'),
    ('Female', 'Female'),
}


def staff_idno():
    """To generate auto increment book ID """
    prfx = "STF"  # prefix of the ID
    last = Staff.objects.all().last()
    if not last:
        stf_id = "{}{}".format(prfx, '0001')
        return stf_id
    last = str(last)
    last = last.replace(' - STF', ', ')
    last = last.split(', ')
    last = last[1]
    last = int(last)
    stf_id = "{}{:04d}".format(prfx, (last + 1))
    return stf_id


class Staff(models.Model):
    """ class of Staff to define entities """
    staff_id = models.CharField(max_length=45, blank=False, unique=True, editable=False, default=staff_idno)
    full_name = models.CharField(max_length=100, blank=False)
    sex = models.CharField(max_length=10, blank=True, null=True, choices=sex_choices)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return "{} - {}".format(self.full_name, self.staff_id)


def book_idno():
    """To generate auto increment book ID """
    prfx = "BK"   # prefix of the ID
    last = Book.objects.all().last()
    if not last:
        bk_id = "{}{}".format(prfx, '0001')
        return bk_id
    last = str(last)
    last = last.replace(' - BK', ', ')
    last = last.split(', ')
    last = last[1]
    last = int(last)
    bk_id = "{}{:04d}".format(prfx, (last + 1))
    return bk_id


class Book(models.Model):
    """ class of Book to define entities """
    book = models.FileField(upload_to='media', blank=False, null=True)
    book_id = models.CharField(max_length=45, blank=False, unique=True, editable=False, default=book_idno)
    book_name = models.CharField(max_length=1000, blank=False)
    author = models.ForeignKey(Author, blank=True, null=True, on_delete=models.CASCADE)
    edition = models.CharField(max_length=1000, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    shelf_id = models.ForeignKey(Shelf, blank=False, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='media', blank=True, default='media/def.jpg')
    staff_id = models.ForeignKey(Staff, blank=False, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True, blank=False, editable=False)

    def __str__(self):
        return "{} - {}".format(self.book_name, self.book_id)


class Blog(models.Model):
    """ Class to post blog """
    title = models.CharField(max_length=100, blank=False, null=True)
    description = models.CharField(max_length=10000, blank=False, null=True)
    photo = models.ImageField(upload_to='media', blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True, auto_now=False, blank=False, null=True)
