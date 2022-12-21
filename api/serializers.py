from rest_framework import serializers
from blog.models import Post, Capitulo


class CapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Capitulo
        fields = ('cap_title', 'cap_body', 'image', 'cita1', 'cita2', 'referencias1',
                  'sub_title1', 'sub_body1', 'image1', 'cita3', 'cita4', 'referencias2',
                  'sub_title2', 'sub_body2', 'image2', 'cita5', 'cita6', 'referencias3',
                  'sub_title3', 'sub_body3', 'image3', 'cita7', 'cita8', 'referencias4',)


class PostSerializer(serializers.ModelSerializer):
    capitulos = CapSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'author', 'abstract', 'importantWords',
                  'body', 'references', 'image', 'image2', 'subject', 'capitulos')
