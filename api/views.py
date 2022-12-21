from rest_framework import generics
from blog.models import Post, Capitulo
from .serializers import PostSerializer, CapSerializer

# Create your views here.


class PostApiView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
