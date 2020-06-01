""""Serializers for Categories"""

from rest_framework import serializers

from users.models import User
from users.serializers import UserSerializer
from .models import Comment


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    """Set the fields to be use in the view file"""
    user = serializers.SerializerMethodField()


    class Meta:
        model = Comment
        fields = ('id', 'content', 'user_id', 'news_id', 'deleted', 'user', 'created')

    def get_user(self, instance):
        queryset = User.objects.get(id=instance.user_id)
        serializer = UserSerializer(queryset, many=False)
        return serializer.data