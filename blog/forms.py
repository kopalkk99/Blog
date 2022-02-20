from django import forms
from blog.models import Post,Comment

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author','post_title','post_desc')

        widgets = {
            'title' : forms.TextInput(attrs={'class':'testinputclass'}),
            'text' : forms.TextInput(attrs={'class':'editable medium-editor-textarea postcontent'})
        }

class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author','comment_desc')

        widgets = {
            'author': forms.TextInput(attrs={'class':'textinputclass'}),
            'comment_desc' : forms.TextInput(attrs={'class':'editable medium-editor-textarea'})
        }
