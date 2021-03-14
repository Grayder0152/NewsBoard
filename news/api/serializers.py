from rest_framework import serializers

from ..models import Article, Comment


class ArticleSerializers(serializers.ModelSerializer):
    """Serializers for articles"""

    title = serializers.CharField(required=True)
    link = serializers.SlugField(required=True)
    text = serializers.CharField(required=False, write_only=True)
    author_name = serializers.CharField(required=True)
    creation_data = serializers.DateField(required=False, read_only=True)
    amount_upvotes = serializers.IntegerField(required=False, default=0)

    class Meta:
        model = Article
        fields = [
            "title",
            "link",
            "creation_data",
            "amount_upvotes",
            "author_name",
            "text"
        ]


class CommentSerializers(serializers.ModelSerializer):
    """Serializers for comments article"""

    id = serializers.IntegerField(required=False, read_only=True)
    author_name = serializers.CharField(required=True)
    content = serializers.CharField(required=True)
    creation_data = serializers.DateField(required=False, read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "author_name", "content", "creation_data", "article"]
