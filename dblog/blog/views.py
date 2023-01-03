
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from blog.serializers import UserSerializer, PostSerializer, TagSerializer
from blog.models import Post

class ListCreateAPIVIEW(ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class UpdateDestroyVIEW(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()