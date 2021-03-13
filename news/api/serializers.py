from rest_framework import serializers

from ..models import Article, Comment


class ArticleSerializers(serializers.ModelSerializer):
    title = serializers.CharField(required=True)
    link = serializers.SlugField(required=True)
    creation_data = serializers.DateField(required=False)
    amount_upvotes = serializers.IntegerField(required=False, default=0)
    author_name = serializers.CharField(required=True)

    class Meta:
        model = Article
        fields = ['title', 'link', 'creation_data', 'amount_upvotes', 'author_name']


class CommentSerializers(serializers.ModelSerializer):
    author_name = serializers.CharField(required=True)
    content = serializers.CharField(required=True)
    creation_data = serializers.DateField(required=False)
    # article = str(serializers.CharField(required=True))

    class Meta:
        model = Comment
        fields = ['author_name', 'content', 'creation_data', 'article']
