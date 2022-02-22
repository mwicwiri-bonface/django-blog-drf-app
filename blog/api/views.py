from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView

from blog.api.serializers import PostSerializer
from blog.models import Post


class PostListCrete(ListCreateAPIView):
    queryset = Post.published_objects.all()
    serializer_class = PostSerializer


class PostRetrieveDestroy(RetrieveDestroyAPIView):
    queryset = Post.objects.all().select_related('category', 'author')
    serializer_class = PostSerializer
