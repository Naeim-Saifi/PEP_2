from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from books.models import Book
from books.serializers import BookSerializer


# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

@api_view(['GET'])
def book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


def book_create(request):
    if request.method == 'POST':
        serializer = BookSerializer(data=request.data)