from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Book
from .serializers import BookSerializer
from rest_framework import generics, status

class BookListApi(APIView):
    def get(self,request):
        books = Book.objects.all()
        serialize_data = BookSerializer(books,many=True).data
        return Response(
            serialize_data,
            status=status.HTTP_200_OK
        )

# class BookListApi(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookDetailView(APIView):
    def get(self,request,pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

# class BookDetailView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookDeleteView (APIView):
    def delete(self,request,pk):
        book = get_object_or_404(Book,pk=pk)
        book.delete()
        return Response({
            "status":True,
            "message": f"{book.title} is deleted successfully"
        },
        status=status.HTTP_200_OK
        )

# class BookDeleteView(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookCreateView(APIView):
    def post(self,request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status":True,
                "message": f"{serializer.data["title"]} book is created successfully",
                "data": serializer.data
            },
            status=status.HTTP_201_CREATED
            )
        return Response({
            "status": False,
            "message": "Bad request",
            "errors": serializer.errors,
        },
        status=status.HTTP_400_BAD_REQUEST
        )

# class BookCreateView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# class BookListCreate(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookListCreate(APIView):
    def get(self,request):
        books = Book.objects.all()
        serializer_data = BookSerializer(books, many=True).data
        return Response({
            "status": True,
            "data": serializer_data
        },
            status=status.HTTP_200_OK
        )

    def post(self,request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )




# class BookUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookUpdateDeleteView(APIView):
    def put(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(instance=book, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "status": True,
                "message": "Book updated successfully",
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )

class BookViewset(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer