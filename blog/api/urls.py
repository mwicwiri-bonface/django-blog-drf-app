from django.urls import path

from blog.api.views import PostListCrete, PostRetrieveDestroy

urlpatterns = [
    path('<int:pk>/', PostRetrieveDestroy.as_view(), name="post-retrieve-destroy"),
    path('', PostListCrete.as_view(), name="post-list-create"),
]
