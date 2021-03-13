from django.contrib import admin
from .models import Article, Comment


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """Article admin"""
    list_display = ('title', 'creation_data', 'amount_upvotes', 'author_name')
    list_display_links = ('title',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Comment admin"""
    list_display = ('id', 'author_name', 'creation_data', 'article')
    list_display_links = ('id',)


admin.site.site_title = 'News Board'
admin.site.site_header = 'News Board'
