from django.db import router
from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import (
    BookListApi,
    BookDetailView,
    BookCreateView,
    BookDeleteView,
    BookListCreate,
    BookUpdateDeleteView,
    BookViewset
)

router = SimpleRouter()
router.register('books',BookViewset,basename='books')

urlpatterns = [
    # path('',BookListApi.as_view()),
    # path('<int:pk>',BookDetailView.as_view()),
    # path('delete/<int:pk>',BookDeleteView.as_view()),
    # path('create',BookCreateView.as_view()),
    # path('get',BookListCreate.as_view()),
    # path('update/<int:pk>',BookUpdateDeleteView.as_view())
]

urlpatterns += router.urls