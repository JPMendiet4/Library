from django.urls import path
from digitallibrary.api.views import *

urlpatterns = [
    path('authors', AuthorViewSet.as_view(), name='Autores'),
    path('author/<int:pk>/', AuthorDetailAPIView.as_view(), name='Autor'),
    path('authors/create', AuthorCreateAPIView.as_view(), name='Crear autor'),
    path('authors/delete/<int:pk>/', AuthorDeleteAPIView.as_view(), name='Eliminar autor'),
    path('authors/update/<int:pk>/', AuthorUpdateAPIView.as_view(), name='Actualizar autor'),
    path('books', BooksViewSet.as_view(), name='Libros'),
    path('books/create', BooksCreateAPIView.as_view(), name='Crear libro'),
    path('book/delete/<int:pk>', BookDeleteAPIView.as_view(), name='Eliminar libro'),
    path('book/update/<int:pk>/', BookUpdateAPIView.as_view(), name='Actualizar libro'),
    path('author-books/<int:pk>/', AuthorBooksView.as_view(), name='Libros de autor')
    ]
