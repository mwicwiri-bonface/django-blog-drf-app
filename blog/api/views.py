from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView

from blog.api.serializers import PostSerializer
from blog.models import Post


class PostListCrete(ListCreateAPIView):
    queryset = Post.published_objects.all().order_by('-created')
    serializer_class = PostSerializer


class PostRetrieveDestroy(RetrieveDestroyAPIView):
    """
    get: Endpoint for getting post details
    delete: endpoint for deleting a post
    """
    queryset = Post.objects.all().select_related('category', 'author').order_by('-created')
    serializer_class = PostSerializer
