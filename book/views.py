from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema

from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework_csv.renderers import CSVRenderer


from book.serializers import BookSerializer
from .models import Book

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    parser_classes = [JSONParser]
    http_method_names = ['get', 'post', 'patch', 'delete']

    @swagger_auto_schema(operation_summary="Create a new book", operation_description="Adds a new book to the collection.")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Retrieve a book by ID", operation_description="Fetches details of a book by its ID.")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Delete a book", operation_description="Removes a book from the collection by its ID.")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Update book info", operation_description="Updates info about a book")
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(method='get', operation_summary="Get all books in CSV", operation_description="Fetches all books in CSV format.")
    @action(detail=False, methods=['get'], renderer_classes=[CSVRenderer])
    def get_all(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)

# Create your views here.
