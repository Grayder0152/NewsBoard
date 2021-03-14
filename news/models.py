from django.db import models


class Article(models.Model):
    """News article on chalkboard"""

    title = models.CharField(
        max_length=64,
        verbose_name="Article title"
    )
    link = models.SlugField(
        max_length=32,
        unique=True
    )
    text = models.TextField(
        verbose_name="Type your article",
        default="Text"
    )
    creation_data = models.DateField(
        auto_now=True,
        auto_created=True
    )
    amount_upvotes = models.PositiveIntegerField(
        default=0,
        blank=True,
        null=True
    )
    author_name = models.CharField(
        max_length=32,
        verbose_name="Author name"
    )

    def __str__(self):
        return f"{self.id}"


class Comment(models.Model):
    """Comment on the article"""

    author_name = models.CharField(
        max_length=32,
        verbose_name="Author name"
    )
    content = models.TextField()
    creation_data = models.DateField(
        auto_now=True,
        auto_created=True
    )
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.id}"
