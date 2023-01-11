from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authentication import authenticate

from digitallibrary.models import Author, Books
from digitallibrary.api.serializers import BooksSerializer, AuthorSerializer
from digitallibrary.api.general_serializer import GeneralListApiView
# Create your views here.


class AuthorViewSet(GeneralListApiView):
    """Read Authors. """
    serializer_class = AuthorSerializer

    def get(self):
        author = self.get_object()
        if author.nationality == '':
            author.nationality = 'Origen desconocido'


class AuthorDetailAPIView(generics.RetrieveAPIView):
    """Read author. """
    allowed_methods = ['get']
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class AuthorCreateAPIView(generics.CreateAPIView):
    """Create author"""
    allowed_methods = ['post']
    serializer_class = AuthorSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Autor agregado correctamente'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorDeleteAPIView(generics.DestroyAPIView):
    """Delete author. """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = 'pk'


class AuthorUpdateAPIView(generics.UpdateAPIView):
    """Update author"""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = 'pk'

    def get(self, request, pk):
        author = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(author)
        return Response(serializer.data)


class BooksViewSet(GeneralListApiView):
    """Read books. """
    serializer_class = BooksSerializer


class BooksCreateAPIView(generics.CreateAPIView):
    """Create book. """
    serializer_class = BooksSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Libro agregado correctamente'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDeleteAPIView(generics.DestroyAPIView):
    """Delete book. """
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    lookup_field = 'pk'

    def delete(self, request):
        book = self.get_object()
        if book.copies > 0:
            book.copies -= 1
            book.save()
            return Response({'copies': book.copies})
        else:
            return super().delete(request)


class BookUpdateAPIView(generics.UpdateAPIView):
    """Update Book"""
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    lookup_field = 'pk'

    def get(self, request, pk):
        author = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(author)
        return Response(serializer.data)
