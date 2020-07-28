from django import forms
from .models import Comment, Post


class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','image','content']