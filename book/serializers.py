from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id","title","subtitle","author","isbn","price"]

    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author',None)
        print(data)
        # check title
        if not title.isalpha():
            raise serializers.ValidationError(
                {
                    "status": False,
                    "message": "The title of the book should only contain symbol!"
                }
            )
        # check unique
        if Book.objects.filter(title=title,author=author).exists():
            raise serializers.ValidationError(
                {
                    "status": False,
                    "message": "You can't add same book many times"
                }
            )
        return data