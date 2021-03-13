from .models import Article
from django.forms import ModelForm, TextInput, Textarea


class ArticleForm(ModelForm):
    """Form for create article"""

    class Meta:
        model = Article
        fields = ["author_name", "title", "link", "text"]
        widgets = {
            "author_name": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter your name"}
            ),
            "title": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter title for article",
                }
            ),
            "link": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter slug for article"}
            ),
            "text": Textarea(
                attrs={"class": "form-control", "placeholder": "Enter text"}
            ),
        }
