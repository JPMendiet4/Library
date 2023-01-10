from rest_framework import serializers
from digitallibrary.models import Author, Books


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('title', 'year', 'language', 'cover_url', 'price', 'sellable', 'copies', 'description', 'author')
        
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'title': instance.title,
            'year': instance.year,
            'language': instance.language,
            'cover_url': instance.cover_url,
            'price': instance.price,
            'sellable': instance.sellable,
            'copies': instance.copies,
            'description': instance.description,
            'author': instance.author.name,
            
        } 

