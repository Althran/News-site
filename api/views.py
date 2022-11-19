from rest_framework.viewsets import ModelViewSet


from .serializers import PostSerializer, CommentSerializer, ContactSerializer
from core.models import Post, Comment, Contact


class PostViewSet(ModelViewSet):
    queryset = Post.objects.filter(is_published=True)
    serializer_class = PostSerializer


class CommentList(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ContactList(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
