from rest_framework.serializers import ModelSerializer
from slugify import slugify

from core.models import Post, Comment, Contact


class PostSerializer(ModelSerializer):

    def create(self, validated_data):
        validated_data.update({'slug': slugify(validated_data.get('title') + validated_data.get('subtitle')) + ' ' + str(validated_data.get('id'))})
        post = Post(**validated_data)
        post.save()
        return post

    class Meta:
        model = Post
        fields = ('id', 'title', 'subtitle', 'text', 'author', 'image')


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post', 'author', 'text']


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'email']
