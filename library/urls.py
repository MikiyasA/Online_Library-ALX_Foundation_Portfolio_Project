from django.conf.urls.static import static
from django.urls import path, include
from . import views
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),
    path('post', views.post_blog, name='post'),

    path('book/<str:pk>/', views.book, name='book'),
    path('addBook', views.add_book, name='addBook'),
    path('updateBook/<str:pk>/', views.update_book, name='updateBook'),

    path('shelf', views.shelf, name='/shelf'),
    path('addShelf', views.add_shelf, name='addShelf'),
    path('updateShelf/<str:pk>/', views.update_shelf, name='updateShelf'),
    path('addAuthor', views.add_author, name='addAuthor'),

    path('contacts', views.contact, name='contacts'),
    path('about/', views.about, name='about'),

    path('accounts/', include('registration.backends.default.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)